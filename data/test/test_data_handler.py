from unittest import TestCase

import pandas as pd

from data.data_processing.data_handler import DataHandler


class TestDataHandler(TestCase):
    def setUp(self):
        self.data_handler = DataHandler()

    def test_raw_data_read(self):
        raw_data = self.data_handler.get_csv_raw_data("all_marcap.csv")

        # raw_data index timestamp인지 확인
        self.assertEqual(type(raw_data.index), pd.DatetimeIndex)

        # raw_data datatype float인지 확인
        self.assertEqual(raw_data.dtypes[0], 'float64')

    def test_상장폐지종목_nan값_제거(self):
        raw_data = self.data_handler.get_csv_raw_data("all_marcap.csv")

        # raw_data의 마지막 row에서 nan값인 column 이름 가져옴
        nan_column_name = raw_data.iloc[-1][raw_data.iloc[-1].isnull()].index[0]

        cleaned_data = self.data_handler.process_nan_to_zero(raw_data)

        # nan값이 제거되었는지 확인
        self.assertEqual(cleaned_data.iloc[-1][nan_column_name], 0)

        print(cleaned_data)
