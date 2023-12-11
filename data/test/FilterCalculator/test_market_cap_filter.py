from unittest import TestCase
import pandas as pd
from data.data_processing.filter_calculator.market_cap_filter import MarketCapFilter
from data.data_processing.data_handler import DataHandler

class TestMarketCapFilter(TestCase):
    def setUp(self):
        self.filter = MarketCapFilter()
        self.data_handler = DataHandler()
        self.real_data = self.get_real_data()
        self.test_data = self.get_test_data()

    def test_get_large_market_cap_filter(self):
        # threshold = 0.25일 때
        threshold = 0.25
        result = self.filter.get_large_market_cap_filter(self.test_data, 3, threshold)
        # Company A True, Company D False
        self.assertEqual(result['CompanyA'][4], True)
        self.assertEqual(result['CompanyD'][4], False)

        threshold = 3
        result = self.filter.get_large_market_cap_filter(self.test_data, 3, threshold)
        # Company A True, Company D False
        self.assertEqual(result['CompanyA'][4], True)
        self.assertEqual(result['CompanyD'][4], False)


    def test_get_small_market_cap_filter(self):
        # threshold = 0.25일 때
        threshold = 0.75
        result = self.filter.get_small_market_cap_filter(self.test_data, 3, threshold)
        # Company A False, Company D True
        self.assertEqual(result['CompanyA'][4], False)
        self.assertEqual(result['CompanyF'][4], True)

        threshold = 3
        result = self.filter.get_small_market_cap_filter(self.test_data, 3, threshold)
        # Company A False, Company D True
        self.assertEqual(result['CompanyA'][4], False)
        self.assertEqual(result['CompanyF'][4], True)

    def get_real_data(self):
        raw_data = self.data_handler.get_csv_raw_data("all_marcap.csv")
        return raw_data

    def get_test_data(self):
        return pd.DataFrame({
            'CompanyA': [1000, 1000, 1000, 1000, 1000],
            'CompanyB': [800, 800, 800, 800, 800],
            'CompanyC': [600, 600, 600, 600, 600],
            'CompanyD': [400, 400, 400, 400, 400],
            'CompanyE': [200, 200, 200, 200, 200],
            'CompanyF': [100, 100, 100, 100, 100],
        })