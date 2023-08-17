import datetime
import os
import time
import exchange_calendars as ecals
import pandas as pd
import pykrx.stock as pystock
import FinanceDataReader as fdr
import tqdm


class CollectData:
    def __init__(self, start_date: str, end_date: str):
        '''
        :param start_date: YYYYmmdd ex. 20200101
        :param end_date: YYYYmmdd ex. 20200101
        '''
        self.start_date = start_date
        self.end_date = end_date
        self.csv_path = os.path.dirname(os.path.abspath(__file__)) + '/csv'
        self.xkrx = ecals.get_calendar('XKRX')

    # 영업일 list 생성
    def generate_date_list(self) -> list:
        start = self.start_date[0:4] + '-' + self.start_date[4:6] + '-' + self.start_date[6:8]
        end = self.end_date[0:4] + '-' + self.end_date[4:6] + '-' + self.end_date[6:8]
        dates = fdr.DataReader('KS11', start, end)
        dates = dates.dropna(how='all') # 전부 NaN 값일 경우 제거
        date_list = dates.index.to_list()
        return date_list

    def generate_and_save_raw_data(self):
        date_list = self.generate_date_list()
        marcap_df = pd.DataFrame(index=date_list)
        price_df = pd.DataFrame(index=date_list)
        volume_df = pd.DataFrame(index=date_list)
        transaction_value_df = pd.DataFrame(index=date_list)

        for date in tqdm.tqdm(date_list):
            kospi_raw_data = self.get_raw_data(date, 'KOSPI')
            kosdaq_raw_data = self.get_raw_data(date, 'KOSDAQ')
            all_raw_data = pd.concat([kospi_raw_data, kosdaq_raw_data])

            kospi_marcap = self.generate_marcap_df(date, kospi_raw_data, marcap_df)
            kosdaq_marcap = self.generate_marcap_df(date, kosdaq_raw_data, marcap_df)
            all_marcap = self.generate_marcap_df(date, all_raw_data, marcap_df)

            kospi_price = self.generate_price_df(date, kospi_raw_data, price_df)
            kosdaq_price = self.generate_price_df(date, kosdaq_raw_data, price_df)
            all_price = self.generate_price_df(date, all_raw_data, price_df)

            kospi_volume = self.generate_volume_df(date, kospi_raw_data, volume_df)
            kosdaq_volume = self.generate_volume_df(date, kosdaq_raw_data, volume_df)
            all_volume = self.generate_volume_df(date, all_raw_data, volume_df)

            kospi_transaction_value = self.generate_transaction_value_df(date, kospi_raw_data, transaction_value_df)
            kosdaq_transaction_value = self.generate_transaction_value_df(date, kosdaq_raw_data, transaction_value_df)
            all_transaction_value = self.generate_transaction_value_df(date, all_raw_data, transaction_value_df)

        save_path = self.csv_path + '/raw_data'

        kospi_marcap.to_csv(save_path + '/kospi_marcap.csv')
        kosdaq_marcap.to_csv(save_path + '/kosdaq_marcap.csv')
        all_marcap.to_csv(save_path + '/all_marcap.csv')

        kospi_price.to_csv(save_path + '/kospi_price.csv')
        kosdaq_price.to_csv(save_path + '/kosdaq_price.csv')
        all_price.to_csv(save_path + '/all_price.csv')

        kospi_volume.to_csv(save_path + '/kospi_volume.csv')
        kosdaq_volume.to_csv(save_path + '/kosdaq_volume.csv')
        all_volume.to_csv(save_path + '/all_volume.csv')

        kospi_transaction_value.to_csv(save_path + '/kospi_transaction_value.csv')
        kosdaq_transaction_value.to_csv(save_path + '/kosdaq_transaction_value.csv')
        all_transaction_value.to_csv(save_path + '/all_transaction_value.csv')

    def generate_marcap_df(self, date: datetime.datetime, new_data: pd.DataFrame,
                           result_data: pd.DataFrame) -> pd.DataFrame:
        '''
        :param new_data: 새로운 데이터
        :param result_data: 기존 데이터
        :return: 새로운 데이터와 기존 데이터를 합친 데이터
        '''
        new_data_t = new_data.T
        code_list = new_data_t.columns.to_list()
        result_data.loc[date, code_list] = new_data_t.loc['시가총액', code_list]

        return result_data

    def generate_volume_df(self, date: datetime.datetime, new_data: pd.DataFrame,
                           result_data: pd.DataFrame) -> pd.DataFrame:
        '''
        :param new_data: 새로운 데이터
        :param result_data: 기존 데이터
        :return: 새로운 데이터와 기존 데이터를 합친 데이터
        '''
        new_data_t = new_data.T
        code_list = new_data_t.columns.to_list()
        result_data.loc[date, code_list] = new_data_t.loc['거래량', code_list]

        return result_data

    def generate_transaction_value_df(self, date: datetime.datetime, new_data: pd.DataFrame,
                                      result_data: pd.DataFrame) -> pd.DataFrame:
        '''
        :param new_data: 새로운 데이터
        :param result_data: 기존 데이터
        :return: 새로운 데이터와 기존 데이터를 합친 데이터
        '''
        new_data_t = new_data.T
        code_list = new_data_t.columns.to_list()
        result_data.loc[date, code_list] = new_data_t.loc['거래대금', code_list]

        return result_data

    def generate_price_df(self, date: datetime.datetime, new_data: pd.DataFrame,
                          result_data: pd.DataFrame) -> pd.DataFrame:
        new_data_t = new_data.T
        code_list = new_data_t.columns.to_list()
        result_data.loc[date, code_list] = new_data_t.loc['종가', code_list]

        return result_data

    def get_raw_data(self, date, market):
        '''
        :param date: YYYY-mm-dd
        :param market: KOSPI, KOSDAQ, KONEX, ALL
        :return:
        '''

        date = date.strftime('%Y%m%d')
        raw_data = pystock.get_market_cap(date, market=market)
        return raw_data


if __name__ == "__main__":
    start_time = datetime.datetime.now()

    start_date = '20060101'
    end_date = '20230731'

    cd = CollectData(start_date, end_date)
    cd.generate_and_save_raw_data()

    end_time = datetime.datetime.now()
    total_time = end_time - start_time

    print('total time : ', total_time.total_seconds() / 60, "min")
