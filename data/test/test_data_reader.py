from unittest import TestCase

from data.data_reader import DataReader


class TestDataReader(TestCase):
    def setUp(self):
        self.data_reader = DataReader()

    def test_get_marcap_parquet(self):
        df = self.data_reader.get_market_cap_parquet()

        print(df.index.dtype)
        print(df.values.dtype)
        print(df.head())

    def test_get_absolute_return_parquet(self):
        df = self.data_reader.get_absolute_return_parquet("1_1")

        print(df.index.dtype)
        print(df.values.dtype)
        print(df.head())

    def test_get_ma_filter_parquet(self):
        df = self.data_reader.get_ma_filter_parquet(5, "1")

        print(df.index.dtype)
        print(df.values.dtype)
        print(df.head())

    def test_get_bband_break_parquet(self):
        df = self.data_reader.get_bband_break_filter_parquet("upper", "1")

        print(df.index.dtype)
        print(df.values.dtype)
        print(df.head())

    def test_get_bband_pct_parquet(self):
        df = self.data_reader.get_bband_pctb_filter_parquet("high", "5")

        print(df.index.dtype)
        print(df.values.dtype)
        print(df.head())