from unittest import TestCase
import numpy as np
import pandas as pd
from backtest.bakctester.momentum_backtest.momentum_strategy_backtester import MomentumStrategyBacktester
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder


class TestMomentumStrategyBacktest(TestCase):
    def setUp(self):
        self.parameter = MomentumParameters()
        self.encoder = ParameterEncoderDecoder(self.parameter)
        self.backtester = MomentumStrategyBacktester(self.parameter, self.encoder)

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

        result_one = self.backtester.is_not_validate_parameter(all_zero_parm)
        result_two = self.backtester.is_not_validate_parameter(all_one_parm)

        self.assertEqual(result_one, False)
        self.assertEqual(result_two, True)

    def test_get_market_cap_filtered_df(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        all_one_parm = np.ones(parm_length)
        parameter_dict = self.encoder.decode_to_index(all_one_parm)

        # test
        result = self.backtester.get_calculated_df.get_market_cap_filter_df(parameter_dict)
        print(result)


    def test_get_volume_filter_df(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        all_one_parm = np.ones(parm_length)
        parameter_dict = self.encoder.decode_to_index(all_one_parm)

        # test
        result = self.backtester.get_calculated_df.get_volume_filter_df(parameter_dict)
        print(result)

    def test_get_transaction_amount_filter_df(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        all_one_parm = np.ones(parm_length)
        parameter_dict = self.encoder.decode_to_index(all_one_parm)

        # test
        result = self.backtester.get_calculated_df.get_transaction_amount_filter_df(parameter_dict)
        print(result)

    def test_get_turn_over_filter_df(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        # random parameter
        random_parm = np.random.rand(parm_length)
        parameter_dict = self.encoder.decode_to_index(random_parm)

        # test
        result = self.backtester.get_calculated_df.get_turn_over_filter_df(parameter_dict)
        print(result)

    def test_get_absolute_return_filter_df(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        # random parameter, 1~3 사이의 정수
        random_parm = np.random.randint(1, 4, parm_length)
        parameter_dict = self.encoder.decode_to_index(random_parm)

        # test
        result = self.backtester.get_calculated_df.get_absolute_return_filter_df(parameter_dict)
        print(result)

    def test_empty_df_mulitply(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        # random parameter, 1~3 사이의 정수
        random_parm = np.random.randint(1, 4, parm_length)
        parameter_dict = self.encoder.decode_to_index(random_parm)

        # test
        result = self.backtester.get_calculated_df.get_absolute_return_filter_df(parameter_dict)
        result2 = result & True

        # result == result 검증
        self.assertTrue(result.equals(result2))

    def test_multiply_versus_and(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        # random parameter, 1~3 사이의 정수
        random_parm = np.random.randint(1, 4, parm_length)
        parameter_dict = self.encoder.decode_to_index(random_parm)

        one_parm = np.ones(parm_length)
        one_dict = self.encoder.decode_to_index(one_parm)

        # test
        result = self.backtester.get_calculated_df.get_absolute_return_filter_df(parameter_dict)
        result2 = self.backtester.get_calculated_df.get_absolute_return_filter_df(one_dict)

        test1 = result & result2
        test2 = result * result2

        # result == result 검증
        self.assertTrue(test1.equals(test2))

    def test_get_ma_break_filter_df(self):
        # sample parameter
        parm_length = self.parameter.get_number_of_parameters()
        # random parameter, 1~2 사이의 정수
        random_parm = np.random.randint(0, 3, parm_length)
        parameter_dict = self.encoder.decode_to_index(random_parm)

        # test
        result = self.backtester.get_calculated_df.get_ma_break_filter_df(parameter_dict)
        print(result)





