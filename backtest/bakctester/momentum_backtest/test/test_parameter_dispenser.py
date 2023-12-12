from unittest import TestCase
import numpy as np
from backtest.bakctester.momentum_backtest.parameter_dispenser import ParameterDispenser
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder
from data.data_reader.data_reader import BackTestDataReader


class TestParameterDispenser(TestCase):
    def setUp(self):
        self.parameter_dispenser = ParameterDispenser()
        self.parameter = MomentumParameters()
        self.encoder = ParameterEncoderDecoder(self.parameter)
        self.temp_parameter = self.get_temp_parameter()
        self.price_df = self.get_price_df()

    def get_price_df(self):
        data_reader = BackTestDataReader()
        price_df = data_reader.get_market_cap_parquet()
        return price_df

    def get_temp_parameter(self):
        parameter_dict = self.parameter.get_parameter_dict()

        # 1~3까지 랜덤으로 이루어진 파라미터 리스트 생성
        length = len(parameter_dict)
        parameter_list = np.random.randint(1, 4, length)

        return parameter_list

    def test_get_momentum_strategy_mom_type_is_zero(self):
        # 첫 값이 0이고 나머지는 1~3까지 랜덤으로 이루어진 파라미터 리스트 생성
        legnth = len(self.temp_parameter)
        temp_parameter = np.zeros(legnth)
        temp_parameter[1:] = self.temp_parameter[1:]
        temp_parameter = list(temp_parameter)

        parameter_dict = self.encoder.decode_to_index(temp_parameter)

        ## parameter_dict가 전부 0이면 테스트 스탑
        if all(value == 0 for value in parameter_dict.values()):
            print("parameter_dict : ", parameter_dict)
            return

        get_momentum_strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict, self.price_df)
        self.assertEqual(get_momentum_strategy, None)

    def test_get_type_one_momentum_strategy(self):
        test_param = [1, 0, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        parameter_dict = self.encoder.decode_to_index(test_param)
        print("parameter_dict : ", parameter_dict)

        get_momentum_strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict, self.price_df)
        self.assertNotEqual(get_momentum_strategy, None)

    def test_get_type_two_momentum_strategy(self):
        test_param = [1, 1, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        parameter_dict = self.encoder.decode_to_index(test_param)
        print("parameter_dict : ", parameter_dict)

        get_momentum_strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict, self.price_df)
        self.assertNotEqual(get_momentum_strategy, None)

    def test_get_type_three_momentum_strategy(self):
        test_param = [1, 2, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        parameter_dict = self.encoder.decode_to_index(test_param)
        print("parameter_dict : ", parameter_dict)

        get_momentum_strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict, self.price_df)
        self.assertNotEqual(get_momentum_strategy, None)


def test_get_type_four_momentum_strategy(self):
    test_param = [1, 3, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    parameter_dict = self.parameter_encoder.decode_to_index(test_param)
    print("parameter_dict : ", parameter_dict)

    get_momentum_strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict, self.price_df)
    self.assertNotEqual(get_momentum_strategy, None)


def test_get_type_five_momentum_strategy(self):
    test_param = [1, 4, 7, 1, 5, 7, 1, 7, 5, 7, 7, 0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    parameter_dict = self.parameter_encoder.decode_to_index(test_param)
    print("parameter_dict : ", parameter_dict)

    get_momentum_strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict, self.price_df)
    self.assertNotEqual(get_momentum_strategy, None)


def test_generate_strategy_name(self):
    self.parameter_dispenser.generate_strategy_name(self.temp_parameter)
