from unittest import TestCase

from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from data.data_processing.backtest_data_builder import BacktestDataBuilder
from data.data_processing.data_handler import DataHandler


class TestBacktestDataBuilder(TestCase):
    def setUp(self):
        self.momentum_parameter = MomentumParameters()
        self.data_handler = DataHandler()
        self.data_builder = BacktestDataBuilder(self.momentum_parameter, self.data_handler)

    def test_raw_data_read(self):
        raw_data = self.data_handler.get_csv_raw_data("all_marcap.csv")

        # file read 여부 확인
        self.assertIsNotNone(raw_data)

    def test_generate_combinations(self):
        generate_combinations = self.data_builder.generate_combinations

        parameter_dict = self.momentum_parameter.get_parameter_dict()

        market_cap_windows = parameter_dict['market_cap_windows']
        market_cap_select_criteria = parameter_dict['market_cap_select_criteria']

        result = generate_combinations(market_cap_windows, market_cap_select_criteria)

        print(result)

    def test_generate_market_cap_filter(self):
        raw_data = self.data_handler.get_csv_raw_data("all_marcap.csv")

        self.data_builder.generate_market_cap_filter(raw_data)
