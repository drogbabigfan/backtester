from unittest import TestCase
from backtest.bakctester.momentum_backtest.momentum_strategy_backtester import MomentumStrategyBacktester
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder


class TestMomentumStrategyBacktest(TestCase):
    def setUp(self):
        self.parameter = MomentumParameters()
        self.encoder = ParameterEncoderDecoder(self.parameter)
        self.momentum_strategy_backtest = MomentumStrategyBacktester(self.parameter, self.encoder)

    def test_run_backtest(self):
        test_param = [1, 1, 6, 1, 5, 7, 1, 7, 5, 7, 7, 3, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        result = self.momentum_strategy_backtest.run_backtest(test_param)

        print(result.stats)
        print(result.loc['cagr'])
        print(result.loc['max_drawdown'])

    def test_evaluation(self):
        self.fail()

    def test_save_backtest_data(self):
        self.fail()

    def test_when_validate(self):
        test_param = [1, 3, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        result = self.momentum_strategy_backtest.is_not_validate_parameter(test_param)
        self.assertEqual(result, False)
