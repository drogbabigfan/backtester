import os

import pandas as pd


class BackTestDataReader:
    def __init__(self):
        self.raw_data_csv_path = os.path.dirname(os.path.abspath(__file__)) + '/../data_collector/csv/raw_data'
        self.raw_data_parquet_path = os.path.dirname(os.path.abspath(__file__)) + '/../data_collector/parquet/raw_data'
        self.processed_data_csv_path = os.path.dirname(
            os.path.abspath(__file__)) + '/../data_processing/processed_data/csv'
        self.processed_data_parquet_path = os.path.dirname(
            os.path.abspath(__file__)) + '/../data_processing/processed_data/parquet'

    def get_market_cap_parquet(self):
        data_path = self.processed_data_parquet_path + "/raw_data/all_marcap.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_absolute_return_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/absolute_return_filter/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_market_cap_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/market_cap_filter/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_calculated_momentum_rank_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/calculated_momentum_rank/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_period_return_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/period_return_filter/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_transaction_amount_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/transaction_amount_filter/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_turn_over_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/turn_over_filter/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_volume_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/volume_filter/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_ma_filter_parquet(self, window: int, file_name: str):
        data_path = self.processed_data_parquet_path + f"/technical_indicator_filter/ma{window}/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_bband_break_filter_parquet(self, upper_lower: str, file_name: str):
        data_path = self.processed_data_parquet_path + f"/technical_indicator_filter/bband_{upper_lower}_break/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_bband_pctb_filter_parquet(self, high_low: str, file_name: str):
        data_path = self.processed_data_parquet_path + f"/technical_indicator_filter/bband_pctb_{high_low}/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_bband_width_filter_parquet(self, high_low: str, file_name: str):
        data_path = self.processed_data_parquet_path + f"/technical_indicator_filter/bband_width_{high_low}/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_ma_negative_arranged_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/technical_indicator_filter/ma_negative_arranged/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data

    def get_ma_positive_arranged_filter_parquet(self, file_name: str):
        data_path = self.processed_data_parquet_path + f"/technical_indicator_filter/ma_positive_arranged/{file_name}.parquet"
        data = pd.read_parquet(data_path)
        return data
