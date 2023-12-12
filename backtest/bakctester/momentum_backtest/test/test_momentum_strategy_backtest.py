from unittest import TestCase
from backtest.bakctester.momentum_backtest.momentum_strategy_backtester import MomentumStrategyBacktester
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder
from db.backtest_result.momentum_strategy.backest_result_service import BacktestResultService
from db.backtest_result.momentum_strategy.backtest_result_handler import BacktestResultHandler


class TestMomentumStrategyBacktest(TestCase):
    def setUp(self):
        self.parameter = MomentumParameters()
        self.encoder = ParameterEncoderDecoder(self.parameter)
        self.momentum_strategy_backtest = MomentumStrategyBacktester(self.parameter, self.encoder)

    def test_run_backtest(self):
        test_param = [1, 1, 6, 1, 5, 7, 1, 7, 5, 7, 7, 3, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        result = self.momentum_strategy_backtest.run_backtest(test_param)

        print(result.stats)
        print(result.stats.T.columns)
        result = result.stats.T
        print(result['cagr'])
        print(result['max_drawdown'])

    def test_evaluation(self):
        test_param = [1, 1, 6, 1, 5, 7, 1, 7, 5, 7, 7, 3, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

        result = self.momentum_strategy_backtest.evaluation(test_param)

        # 결과값 0이 아닌지 확인
        self.assertEqual(result, 0)

    def test_when_validate(self):
        test_param = [1, 3, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        result = self.momentum_strategy_backtest.is_not_validate_parameter(test_param)
        self.assertEqual(result, False)
