import unittest
import pandas as pd


class TestUtils(unittest.TestCase):
    def get_test_data(self, data_length: int):
        return pd.DataFrame({
            'CompanyA': [1000] * data_length,
            'CompanyB': [800] * data_length,
            'CompanyC': [600] * data_length,
            'CompanyD': [400] * data_length,
            'CompanyE': [200] * data_length,
            'CompanyF': [100] * data_length,
        })



