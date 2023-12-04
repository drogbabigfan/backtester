from unittest import TestCase
from backtest.parameter.momentum_parameters import MomentumParameters

class TestMomentumParameters(TestCase):
    def setUp(self):
        self.momentum_parameter = MomentumParameters()

    def test_get_rebalacne_periods(self):
        rebalance_periods_index = self.momentum_parameter.get_rebalance_peridos_index()
        print("rebalance_periods_index : ", rebalance_periods_index)

        for idx in rebalance_periods_index:
            print("rebalance_periods : ", self.momentum_parameter.get_rebalance_periods(idx))

    def test_get_momentum_windows(self):
        momentum_windows_index = self.momentum_parameter.get_momentum_windows_index()
        print("momentum_windows_index : ", momentum_windows_index)

        for idx in momentum_windows_index:
            print("momentum_windows : ", self.momentum_parameter.get_momentum_windows(idx))


    def test_parameter_length(self):
        legnth = self.momentum_parameter.get_number_of_parameters()
        length2 = len(self.momentum_parameter.get_parameter_dict())
        print("legnth : ", legnth, length2)