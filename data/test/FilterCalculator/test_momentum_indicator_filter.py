from unittest import TestCase
from data.data_processing.data_handler import DataHandler
from data.data_processing.FilterCalculator.market_cap_filter import MarketCapFilter
from data.data_processing.FilterCalculator.momentum_filter import MomentumFilter
from data.test.FilterCalculator.utils import TestUtils


class TestMomentumIndicator(TestCase):
    def setUp(self):
        self.momentum_filter = MomentumFilter()
        self.market_cap_filter = MarketCapFilter()
        self.real_data = DataHandler().get_csv_raw_data("all_marcap.csv")
        self.utils = TestUtils()
        self.test_data = self.utils.get_test_data(250)

    def test_calculate_period_return(self):
        window = 20
        expected_result = 0
        result = self.momentum_filter.calculate_period_return(self.test_data, window)

        self.assertEqual(expected_result, result['CompanyA'][30])

    def test_get_type_one_momentum(self):
        universe = self.market_cap_filter.get_large_market_cap_filter(self.real_data, 20, 0.1)
        universe_expect = universe['005930'].iloc[-1]  # 수정된 코드
        universe_real = universe['005930'].iloc[-1]  # 수정된 코드
        self.assertEqual(universe_expect, universe_real)

        price = self.real_data
        window = 20
        up_or_down = "up"
        threshold = 0.1

        result = self.momentum_filter.get_type_one_momentum(universe, price, window, up_or_down, threshold)
        true_values_in_last_row = result.iloc[-1][result.iloc[-1] == True]
        print(true_values_in_last_row)

    def test_get_type_two_momentum(self):
        universe = self.market_cap_filter.get_large_market_cap_filter(self.real_data, 20, 0.1)
        price = self.real_data
        window = 20
        up_or_down = "up"
        threshold = 0.1

        result = self.momentum_filter.get_type_two_momentum(universe, price, window, up_or_down, threshold)
        true_values_in_last_row = result.iloc[-1][result.iloc[-1] == True]
        print(true_values_in_last_row)

    def test_get_type_three_momentum(self):
        universe = self.market_cap_filter.get_large_market_cap_filter(self.real_data, 20, 0.1)
        price = self.real_data
        window = 20
        up_or_down = "up"

        threshold = 0.1

        result = self.momentum_filter.get_type_three_momentum(universe, price, window, up_or_down, threshold)
        true_values_in_last_row = result.iloc[-1][result.iloc[-1] == True]
        print(true_values_in_last_row)

    def test_get_type_four_momentum(self):
        universe = self.market_cap_filter.get_large_market_cap_filter(self.real_data, 20, 0.1)
        price = self.real_data
        window = 20
        up_or_down = "up"
        threshold = 0.1

        result = self.momentum_filter.get_type_four_momentum(universe, price, window, up_or_down, threshold)
        true_values_in_last_row = result.iloc[-1][result.iloc[-1] == True]
        print(true_values_in_last_row)


    def test_get_type_five_momentum(self):
        universe = self.market_cap_filter.get_large_market_cap_filter(self.real_data, 20, 0.1)
        price = self.real_data
        window = 20
        up_or_down = "up"
        threshold = 0.1

        result = self.momentum_filter.get_type_five_momentum(universe, price, window, up_or_down, threshold)
        true_values_in_last_row = result.iloc[-1][result.iloc[-1] == True]
        print(true_values_in_last_row)

    def test_get_calculate_return_plus(self):
        window = 5
        expected_result = False

        result = self.momentum_filter.get_calculate_return_plus(self.test_data, window)
        self.assertEqual(expected_result, result['CompanyA'][30])

    def test_get_calculate_return_minus(self):
        window = 5
        expected_result = False

        result = self.momentum_filter.get_calculate_return_minus(self.test_data, window)
        self.assertEqual(expected_result, result['CompanyA'][30])
