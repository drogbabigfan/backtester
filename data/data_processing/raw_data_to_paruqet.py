import os

import pandas as pd

from data.data_processing.data_handler import DataHandler


class RawDataToParquet:
    def __init__(self):
        self.data_handler = DataHandler()
        self.processed_data_parquet_path = os.path.dirname(
            os.path.abspath(__file__)) + '/processed_data/parquet/raw_data'

    def csv_to_parquet(self):
        raw_data_path = self.data_handler.raw_data_csv_path + "/raw_data"
        raw_data_list = self.data_handler.read_file_list(raw_data_path)
        for file_name in raw_data_list:
            print(f"processing {file_name}")
            raw_data = self.data_handler.get_csv_raw_data(file_name)

            if self.check_need_downsize(file_name):
                raw_data = self.downsize(raw_data)

            raw_data.to_parquet(self.processed_data_parquet_path + f"/{file_name[:-4]}.parquet")
            print(f"{file_name} is saved as parquet file.")

    def check_need_downsize(self, file_name: str):
        # 파일명에 marcap, transaction, volume이 포함되어 있으면 downsize 필요
        if "marcap" in file_name or "transaction" in file_name or "volume" in file_name:
            return True
        else:
            return False

    def downsize(self, df: pd.DataFrame):
        df = df / 100_000_000
        return df

if __name__ == "__main__":
    raw_data_to_parquet = RawDataToParquet()
    raw_data_to_parquet.csv_to_parquet()