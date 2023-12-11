from unittest import TestCase

import numpy as np

from backtest.bakctester.momentum_strategy_backtester import MomentumStrategyBacktest
from backtest.parameter.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder


class TestMomentumStrategyBacktest(TestCase):
    def setUp(self):
        self.parameter = MomentumParameters()
        self.encoder = ParameterEncoderDecoder(self.parameter)
        self.backtester = MomentumStrategyBacktest(self.parameter, self.encoder)

    def test_run_backetst(self):
        self.fail()

    def test_evaluation(self):
        self.fail()

    def test_save_backtest_data(self):
        self.fail()

    def test_validate_parameter(self):
        parm_length = self.parameter.get_number_of_parameters()

        # sampel paramter
        all_zero_parm = np.zeros(parm_length)
        all_one_parm = np.ones(parm_length)

        result_one = self.backtester.validate_parameter(all_zero_parm)
        result_two = self.backtester.validate_parameter(all_one_parm)

        self.assertEqual(result_one, False)
        self.assertEqual(result_two, True)
