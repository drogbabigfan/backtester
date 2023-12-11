from unittest import TestCase

import numpy as np

from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder
class TestMomentumParameters(TestCase):
    def setUp(self):
        self.momentum_parameter = MomentumParameters()
        self.parameter_encoder = ParameterEncoderDecoder(self.momentum_parameter)

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

    def test_decode(self):
        parameter_dict = self.momentum_parameter.get_parameter_dict()
        print("parameter_dict : ", parameter_dict)

        # 0부터 2까지로 랜덤하게 이루어진 총 길이 33개의 임의의 parmaeter list 생성
        length = len(parameter_dict)
        parameter_list = np.random.randint(0, 3, length)

        # decode
        decoded_parameter = self.parameter_encoder.decode_to_value(parameter_list)
        print("decoded_parameter : ", decoded_parameter)
