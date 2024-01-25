import itertools
import pandas as pd
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters


class ParameterSetGenerator:
    def __init__(self, parameter_object: MomentumParameters):
        self.parameter_object = parameter_object

    def generate_combinations(self):
        rebalacne_periods = list(range(len(self.parameter_object.rebalance_periods)))
        momentum_types = list(range(len(self.parameter_object.momentum_types)))
        momentum_windows = self.parameter_object.momentum_windows.keys()
        momentum_select_criteria = self.parameter_object.momentum_select_criteria.keys()
        momentum_select_counts = self.parameter_object.momentum_select_counts.keys()

        # 시가총액 선택 조건
        market_cap_windows = self.parameter_object.market_cap_windows.keys()
        market_cap_select_criteria = self.parameter_object.market_cap_select_criteria.keys()
        market_cap_select_counts = self.parameter_object.market_cap_select_counts.keys()

        # 거래량 선택 조건
        volume_windows = self.parameter_object.volume_windows.keys()
        volume_select_counts = self.parameter_object.volume_select_counts.keys()

        # 거래대금
        transaction_amount_windows = self.parameter_object.transaction_amount_windows.keys()
        transaction_amount_select_counts = self.parameter_object.transaction_amount_select_counts.keys()

        # 거래회전율
        turn_over_windows = self.parameter_object.turn_over_windows.keys()
        turn_over_select_counts = self.parameter_object.turn_over_select_counts.keys()

        # 절대 모멘텀
        absolute_return_windows = self.parameter_object.absolute_return_windows.keys()
        absolute_return_select_criteria = self.parameter_object.absolute_return_select_criteria.keys()

        # # 기술적지표
        # ma5_break = self.parameter_object.ma5_break.keys()
        # ma10_break = self.parameter_object.ma10_break.keys()
        # ma20_break = self.parameter_object.ma20_break.keys()
        # ma60_break = self.parameter_object.ma60_break.keys()
        # ma120_break = self.parameter_object.ma120_break.keys()
        # ma250_break = self.parameter_object.ma250_break.keys()
        #
        # # bband_break
        # bband_upper_break = self.parameter_object.bband_upper_break.keys()
        # bband_lower_break = self.parameter_object.bband_lower_break.keys()
        #
        # # bband_width
        # bband_width_high = self.parameter_object.bband_width_high.keys()
        # bband_width_low = self.parameter_object.bband_width_low.keys()
        #
        # # bband_pctb
        # bband_pctb_high = self.parameter_object.bband_pctb_high.keys()
        # bband_pctb_low = self.parameter_object.bband_pctb_low.keys()
        #
        # # ma arragned
        # ma_positive_arranged = self.parameter_object.ma_positive_arranged.keys()
        # ma_negative_arranged = self.parameter_object.ma_negative_arranged.keys()

        parameter_combinations = list(itertools.product(rebalacne_periods, # 0
                                                        momentum_types, # 1
                                                        momentum_windows, # 2
                                                        momentum_select_criteria, # 3
                                                        momentum_select_counts, # 4
                                                        market_cap_windows, # 5
                                                        market_cap_select_criteria, # 6
                                                        market_cap_select_counts, # 7
                                                        volume_windows, # 8
                                                        volume_select_counts, # 9
                                                        transaction_amount_windows, # 10
                                                        transaction_amount_select_counts, # 11
                                                        turn_over_windows,
                                                        turn_over_select_counts,
                                                        absolute_return_windows,
                                                        absolute_return_select_criteria,
                                                        # ma5_break,
                                                        # ma10_break,
                                                        # ma20_break,
                                                        # ma60_break,
                                                        # ma120_break,
                                                        # ma250_break,
                                                        # bband_upper_break,
                                                        # bband_lower_break,
                                                        # bband_width_high,
                                                        # bband_width_low,
                                                        # bband_pctb_high,
                                                        # bband_pctb_low,
                                                        # ma_positive_arranged,
                                                        # ma_negative_arranged))
                                                        ))

        return parameter_combinations

    # 제약조건에 맞는 값 추출
    def delete_non_validate_parameter_combination(self, parameter_combinations: list):
        data = []
        for combo in parameter_combinations:
            volume_window = combo[8]
            volume_count = combo[9]
            transaction_amount_window = combo[10]
            transaction_amount_count = combo[11]
            turn_over_window = combo[12]
            turn_over_count = combo[13]
            absolute_return_window = combo[14]
            absolute_return_criteria = combo[15]
            # bband_upper_break = combo[22]
            # bband_lower_break = combo[23]
            # bband_width_high = combo[24]
            # bband_width_low = combo[25]
            # bband_pctb_high = combo[26]
            # bband_pctb_low = combo[27]
            # ma_positive_arranged = combo[28]
            # ma_negative_arranged = combo[29]

            volume_cond = (volume_window == 0 and volume_count == 0) or (volume_window != 0 and volume_count != 0)
            transaction_amount_cond = (transaction_amount_window == 0 and transaction_amount_count == 0) or (
                        transaction_amount_window != 0 and transaction_amount_count != 0)
            turn_over_cond = (turn_over_window == 0 and turn_over_count == 0) or (
                        turn_over_window != 0 and turn_over_count != 0)

            absolute_return_cond = (absolute_return_window == 0 and absolute_return_criteria == 1) or (
                        absolute_return_window != 0)

            # bband_break_cond = (bband_upper_break == 0 and bband_lower_break == 0) or not (
            #             bband_upper_break != 0 and bband_lower_break != 0)
            #
            # bband_width_cond = (bband_width_high == 0 and bband_width_low == 0) or not (
            #             bband_width_high != 0 and bband_width_low != 0)
            #
            # bband_pctb_cond = (bband_pctb_high == 0 and bband_pctb_low == 0) or not (
            #             bband_pctb_high != 0 and bband_pctb_low != 0)
            #
            # ma_arranged_cond = (ma_positive_arranged == 0 and ma_negative_arranged == 0) or not (
            #             ma_positive_arranged == 1 and ma_negative_arranged == 1)

            if (
                volume_cond and transaction_amount_cond and turn_over_cond and absolute_return_cond and bband_break_cond
                    # and bband_width_cond and bband_pctb_cond and ma_arranged_cond
            ):
                data.append(combo)

        df = pd.DataFrame(data, columns=self.parameter_object.get_parameter_dict().keys())
        return df


if __name__ == '__main__':
    generator = ParameterSetGenerator(MomentumParameters())
    combinations = generator.generate_combinations()
    df = generator.delete_non_validate_parameter_combination(combinations)
    print(df)

    df.to_parquet('moment'
                  'um_parameter_set.parquet', index=False)
    df.to_csv('momentum_parameter_set.csv', index=False)



