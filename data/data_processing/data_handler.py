import os
from typing import Any, Union
import pandas as pd
from pandas import Series, DataFrame


class DataHandler:
    def __init__(self):
        self.raw_data_csv_path = os.path.dirname(os.path.abspath(__file__)) + '/../data_collector/csv'
        self.raw_data_parquet_path = os.path.dirname(os.path.abspath(__file__)) + '/../data_collector/parquet'
        self.processed_data_csv_path = os.path.dirname(os.path.abspath(__file__)) + '/processed_data/csv'
        self.processed_data_parquet_path = os.path.dirname(os.path.abspath(__file__)) + '/processed_data/parquet'

    def get_csv_raw_data(self, file_name: str):
        ## file_name 확장자까지 다 필요함
        raw_data_path = self.raw_data_csv_path + f"/raw_data/{file_name}"

        if os.path.isfile(raw_data_path):
            raw_data = pd.read_csv(raw_data_path, index_col=0, header=0, encoding='utf-8-sig', dtype=str)

            columns = raw_data.columns.astype(str)
            raw_data.columns = columns
            raw_data = raw_data.astype(float)

            idx = raw_data.index
            idx = pd.to_datetime(idx)
            raw_data.index = idx

            return raw_data
        else:
            print(f"{file_name} does not exist.")

    def read_file_list(self, folder_path: str):
        file_list = os.listdir(folder_path)
        return file_list

    @staticmethod
    def process_nan_to_zero(df: pd.DataFrame):
        for column in df.columns:
            first_valid_index = df[column].first_valid_index()

            # 첫번째 유효값 이후의 nan값들만 0으로 변경
            df.loc[first_valid_index:, column] = df.loc[first_valid_index:, column].fillna(0)

        return df

    def remove_turnover(self, transaction_value_df: pd.DataFrame, marcap_df: pd.DataFrame, threshold: float):
        turnover_df = transaction_value_df / marcap_df
        result = marcap_df[turnover_df >= threshold] # 회전율 n% 이상
        return result

    def remove_low_transaction_value(self, transaction_value_df: pd.DataFrame, threshold: float,
                                     marcap_df: pd.DataFrame):
        result = marcap_df[transaction_value_df >= threshold] # 거래대금 n억 이상
        return result

    def remove_low_volume(self, volume_df: pd.DataFrame, threshold: float, marcap_df: pd.DataFrame):
        result = marcap_df[volume_df >= threshold] # 거래량 n주 이상
        return result

    def remove_penny_stock(self, price_df: pd.DataFrame, threshold: int, marcap_df: pd.DataFrame):
        result = marcap_df[price_df >= threshold] # 가격 n원 이상
        return result

    def calculate_rank(self, df: pd.DataFrame):
        # 일자기준 rank
        result = df.rank(axis=1, ascending=False, method='min')
        return result

