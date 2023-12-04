from backtest.parameter.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder
from backtest.strategy.strategy_generator import StrategyGenerator


class MomentumStrategyBacktest:
    def __init__(self, parameter: MomentumParameters, parameter_encoder: ParameterEncoderDecoder):
        self.parameter = parameter
        self.strategy_generator = StrategyGenerator()
        self.parameter_encoder = parameter_encoder

    def run_backetst(self, parameter_list: list):
        if self.validate_parameter(parameter_list):
            return 0

        parameter_dict = self.parameter_encoder.decode(parameter_list)

        # select df 생성 -> 미리 계산된 file 읽어서 사용


    def evaluation(self, cagr: float, mdd: float):
        score = cagr - 2 * mdd
        return score

    def save_backtest_data(self):
        # parameter값 db에 저장 -> backtest 결과 db에 저장
        pass

    # parameter 검증
    def validate_parameter(self, paramter_list: list):
        parameter_dict = self.parameter_encoder.decode(paramter_list)

        # rebalance 주기가 0인 경우
        if parameter_dict['rebalance_periods'] == 0:
            return True

        # market cap == small and (volume == small or transaction == samll or turn_over == small) 인 경우
        if parameter_dict['market_cap_select_criteria'] == 'small' and (
                parameter_dict['volume_select_criteria'] == 'small'
                or parameter_dict['transaction_select_criteria'] == 'small' or
                parameter_dict['turn_over_select_criteria'] == 'small'):
            return True

        # 불가능한 case1. 정배열 역배열 동시에 true
        if (parameter_dict['ma_positive_arranged'] == True) and (parameter_dict['ma_negative_arranged'] == True):
            return True

        # 볼밴 upper, lower 동시인 경우
        if parameter_dict['bband_upper_break'] != 0 and parameter_dict['bband_lower_break'] != 0:
            return True

        # 볼밴 bband_width_high와 bband_with_low가 둘다 0이 아닌경우
        if parameter_dict['bband_width_high'] != 0 and parameter_dict['bband_width_low'] != 0:
            return True

        # bband_pctb_high와 bband_pctb_low가 둘다 0이 아닌경우
        if parameter_dict['bband_pctb_high'] != 0 and parameter_dict['bband_pctb_low'] != 0:
            return True

        return False
