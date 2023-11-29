from unittest import TestCase

import numpy as np

from data.data_processing.FilterCalculator.technical_indicator_filter import TechnicalIndicatorFilter
from data.test.FilterCalculator.utils import TestUtils


class TestTechnicalIndicatorFilter(TestCase):
    def setUp(self):
        self.filter = TechnicalIndicatorFilter()
        self.utils = TestUtils()
        self.test_data = self.utils.get_test_data(250)

    def test_calculate_moving_average(self):
        window = 3
        expected_result = 1000
        result = self.filter.calculate_moving_average(self.test_data, window)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_calculate_standard_deviation(self):
        window = 3
        expected_result = 0
        result = self.filter.calculate_standard_deviation(self.test_data, window)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_calculate_ma_disparity(self):
        window = 3
        expected_result = 100
        result = self.filter.calculate_ma_disparity(self.test_data, window)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_calculate_upper_bollinger_band(self):
        window = 3
        multiple = 2
        expected_result = 1000

        result = self.filter.calculate_upper_bollinger_band(self.test_data, window, multiple)
        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_calculate_lower_bollinger_band(self):
        window = 3
        multiple = 2
        expected_result = 1000

        result = self.filter.calculate_lower_bollinger_band(self.test_data, window, multiple)
        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_calculate_bollinger_band_width(self):
        window = 3
        multiple = 2
        expected_result = 0

        result = self.filter.calculate_bollinger_band_width(self.test_data, window, multiple)
        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_calculate_bollinger_band_pctb(self):
        window = 20
        multiple = 2
        expected_result = np.nan # upper=lower인 경우라 nan

        result = self.filter.calculate_bollinger_band_pctb(self.test_data, window, multiple)
        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_get_ma_upper_breakout(self):
        window = 3
        expected_result = False

        result = self.filter.get_ma_upper_breakout(self.test_data, window)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_get_ma_lower_breakout(self):
        window = 3
        expected_result = False

        result = self.filter.get_ma_lower_breakout(self.test_data, window)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_get_bollinger_band_upper_breakout(self):
        window = 3
        multiple = 2
        expected_result = False

        result = self.filter.get_bollinger_band_upper_breakout(self.test_data, window, multiple)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_get_bollinger_band_lower_breakout(self):
        window = 3
        multiple = 2
        expected_result = False

        result = self.filter.get_bollinger_band_lower_breakout(self.test_data, window, multiple)

        self.assertEqual(expected_result, result['CompanyA'][4])

    def test_is_disparity_high(self):
        window = 3
        pct = 105
        expected_result = False
        result = self.filter.is_disparity_high(self.test_data, window, pct)

        pct2 = 95
        expected_result2 = True
        result2 = self.filter.is_disparity_high(self.test_data, window, pct2)

        self.assertEqual(expected_result, result['CompanyA'][4])
        self.assertEqual(expected_result2, result2['CompanyA'][4])

    def test_is_disparity_low(self):
        window = 3
        pct = 95
        expected_result = False
        result = self.filter.is_disparity_low(self.test_data, window, pct)

        pct2 = 105
        expected_result2 = True
        result2 = self.filter.is_disparity_low(self.test_data, window, pct2)

        self.assertEqual(expected_result, result['CompanyA'][4])
        self.assertEqual(expected_result2, result2['CompanyA'][4])

    def test_is_bollinger_band_width_high(self):
        window = 3
        pct = 105
        multiple = 2
        expected_result = False
        result = self.filter.is_bollinger_band_width_high(self.test_data, window, pct, multiple)

        pct2 = 95
        expected_result2 = False
        result2 = self.filter.is_bollinger_band_width_high(self.test_data, window, pct2, multiple)

        self.assertEqual(expected_result, result['CompanyA'][4])
        self.assertEqual(expected_result2, result2['CompanyA'][4])

    def test_is_bollinger_band_width_low(self):
        window = 3
        pct = 95
        multiple = 2
        expected_result = True
        result = self.filter.is_bollinger_band_width_low(self.test_data, window, pct, multiple)

        pct2 = 105
        expected_result2 = True
        result2 = self.filter.is_bollinger_band_width_low(self.test_data, window, pct2, multiple)

        self.assertEqual(expected_result, result['CompanyA'][4])
        self.assertEqual(expected_result2, result2['CompanyA'][4])

    def test_is_ma_positive_arranged(self):
        expected = False
        result = self.filter.is_ma_positive_arranged(self.test_data)

        self.assertEqual(expected, result['CompanyA'][200])

    def test_is_ma_negative_arranged(self):
        expected = False
        result = self.filter.is_ma_negative_arranged(self.test_data)

        self.assertEqual(expected, result['CompanyA'][200])
