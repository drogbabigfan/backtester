class MomentumParameters:
    def __init__(self):
        # 백테스팅 실행 주기
        self.rebalance_periods = list(range(1, 13))
        # momentum 선택 조건
        self.momentum_types = list(range(1, 6))
        self.momentum_windows = {1: 5, 2: 10, 3: 20, 4: 40, 5: 60, 6: 120, 7: 250}
        self.momentum_select_criteria = {1: 'up', 2: 'down'}
        self.momentum_select_counts = {1: 5, 2: 10, 3: 20, 4: 40, 5: 50, 6: 0.005, 7: 0.01, 8: 0.05, 9: 0.1, 10: 0.15,
                                       11: 0.2, 12: 0.3}
        # 시가총액 선택 조건
        self.market_cap_windows = {1: 5, 2: 10, 3: 20, 4: 40, 5: 60, 6: 120, 7: 250}
        self.market_cap_select_criteria = {1: 'large', 2: 'small'}
        self.market_cap_select_counts = {1: 0.01, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.3, 6: 0.4, 7: 0.5}

        # 거래량 선택 조건
        self.volume_windows = {0: 0, 1: 5, 2: 10, 3: 20, 4: 40, 5: 60, 6: 120, 7: 250}
        self.volume_select_criteria = {0: 0, 1: 'large', 2: 'small'}
        self.volume_select_counts = {0: 0, 1: 0.01, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.3, 6: 0.4, 7: 0.5}

        # 거래대금 선택 조건
        self.transaction_amount_windows = {0: 0, 1: 5, 2: 10, 3: 20, 4: 40, 5: 60, 6: 120, 7: 250}
        self.transaction_amount_select_criteria = {0: 0, 1: 'large', 2: 'small'}
        self.transaction_amount_select_counts = {0: 0, 1: 0.01, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.3, 6: 0.4, 7: 0.5}

        # 거래회전율 선택 조건
        self.turn_over_windows = {0: 0, 1: 5, 2: 10, 3: 20, 4: 40, 5: 60, 6: 120, 7: 250}
        self.turn_over_select_criteria = {0: 0, 1: 'large', 2: 'small'}
        self.turn_over_select_counts = {0: 0, 1: 0.01, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.3, 6: 0.4, 7: 0.5}

        # 절대수익률 선택 조건
        self.absolute_return_windows = {0: 0, 1: 5, 2: 10, 3: 20, 4: 40, 5: 60, 6: 120, 7: 250}
        self.absolute_return_select_criteria = {1: 'positive', 2: 'negative'}

        # 기술적지표 선택 조건
        self.ma5_break = {0: 0, 1: 'upper', 2: 'lower'}
        self.ma10_break = {0: 0, 1: 'upper', 2: 'lower'}
        self.ma20_break = {0: 0, 1: 'upper', 2: 'lower'}
        self.ma60_break = {0: 0, 1: 'upper', 2: 'lower'}
        self.ma120_break = {0: 0, 1: 'upper', 2: 'lower'}
        self.ma250_break = {0: 0, 1: 'upper', 2: 'lower'}

        self.bband_upper_break = {0: 0, 1: 2, 2: 2.5, 3: 3}
        self.bband_lower_break = {0: 0, 1: 2, 2: 2.5, 3: 3}

        self.bband_width_high = {0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}
        self.bband_width_low = {0: 0, 1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}

        self.bband_pctb_high = {0: 0, 1: 50, 2: 60, 3: 70, 4: 80, 5: 90}
        self.bband_pctb_low = {0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

        self.ma_positive_arranged = {0: False, 1: True}
        self.ma_negative_arranged = {0: False, 1: True}

    def get_parameter_dict(self) -> dict:
        return {
            'rebalance_periods': self.rebalance_periods,
            'momentum_types': self.momentum_types,
            'momentum_windows': self.momentum_windows,
            'momentum_select_criteria': self.momentum_select_criteria,
            'momentum_select_counts': self.momentum_select_counts,
            'market_cap_windows': self.market_cap_windows,
            'market_cap_select_criteria': self.market_cap_select_criteria,
            'market_cap_select_counts': self.market_cap_select_counts,
            'volume_windows': self.volume_windows,
            'volume_select_criteria': self.volume_select_criteria,
            'volume_select_counts': self.volume_select_counts,
            'transaction_amount_windows': self.transaction_amount_windows,
            'transaction_amount_select_criteria': self.transaction_amount_select_criteria,
            'transaction_amount_select_counts': self.transaction_amount_select_counts,
            'turn_over_windows': self.turn_over_windows,
            'turn_over_select_criteria': self.turn_over_select_criteria,
            'turn_over_select_counts': self.turn_over_select_counts,
            'absolute_return_windows': self.absolute_return_windows,
            'absolute_return_select_criteria': self.absolute_return_select_criteria,
            'ma5_break': self.ma5_break,
            'ma10_break': self.ma10_break,
            'ma20_break': self.ma20_break,
            'ma60_break': self.ma60_break,
            'ma120_break': self.ma120_break,
            'ma250_break': self.ma250_break,
            'bband_upper_break': self.bband_upper_break,
            'bband_lower_break': self.bband_lower_break,
            'bband_width_high': self.bband_width_high,
            'bband_width_low': self.bband_width_low,
            'bband_pctb_high': self.bband_pctb_high,
            'bband_pctb_low': self.bband_pctb_low,
            'ma_positive_arranged': self.ma_positive_arranged,
            'ma_negative_arranged': self.ma_negative_arranged
        }

    def get_number_of_parameters(self) -> int:
        keys = self.get_parameter_dict().keys()
        return len(keys)

    def get_rebalance_periods(self, number: int) -> int:
        return self.rebalance_periods[number]

    def get_momentum_types(self, number: int) -> int:
        return self.momentum_types[number]

    def get_momentum_windows(self, number: int) -> int:
        return self.momentum_windows[number]

    def get_momentum_select_criteria(self, number: int) -> str:
        return self.momentum_select_criteria[number]

    def get_momentum_select_counts(self, number: int) -> float:
        return self.momentum_select_counts[number]

    def get_market_cap_windows(self, number: int) -> int:
        return self.market_cap_windows[number]

    def get_market_cap_select_criteria(self, number: int) -> str:
        return self.market_cap_select_criteria[number]

    def get_market_cap_select_counts(self, number: int) -> float:
        return self.market_cap_select_counts[number]

    def get_volume_windows(self, number: int) -> int:
        return self.volume_windows[number]

    def get_volume_select_criteria(self, number: int) -> str:
        return self.volume_select_criteria[number]

    def get_volume_select_counts(self, number: int) -> float:
        return self.volume_select_counts[number]

    def get_transaction_amount_windows(self, number: int) -> int:
        return self.transaction_amount_windows[number]

    def get_transaction_amount_select_criteria(self, number: int) -> str:
        return self.transaction_amount_select_criteria[number]

    def get_transaction_amount_select_counts(self, number: int) -> float:
        return self.transaction_amount_select_counts[number]

    def get_turn_over_windows(self, number: int) -> int:
        return self.turn_over_windows[number]

    def get_turn_over_select_criteria(self, number: int) -> str:
        return self.turn_over_select_criteria[number]

    def get_turn_over_select_counts(self, number: int) -> float:
        return self.turn_over_select_counts[number]

    def get_absolute_return_windows(self, number: int) -> int:
        return self.absolute_return_windows[number]

    def get_absolute_return_select_criteria(self, number: int) -> str:
        return self.absolute_return_select_criteria[number]

    def get_ma5_break(self, number: int) -> str:
        return self.ma5_break[number]

    def get_ma10_break(self, number: int) -> str:
        return self.ma10_break[number]

    def get_ma20_break(self, number: int) -> str:
        return self.ma20_break[number]

    def get_ma60_break(self, number: int) -> str:
        return self.ma60_break[number]

    def get_ma120_break(self, number: int) -> str:
        return self.ma120_break[number]

    def get_ma250_break(self, number: int) -> str:
        return self.ma250_break[number]

    def get_bband_upper_break(self, number: int) -> float:
        return self.bband_upper_break[number]

    def get_bband_lower_break(self, number: int) -> float:
        return self.bband_lower_break[number]

    def get_bband_width_high(self, number: int) -> float:
        return self.bband_width_high[number]

    def get_bband_width_low(self, number: int) -> float:
        return self.bband_width_low[number]

    def get_bband_pctb_high(self, number: int) -> float:
        return self.bband_pctb_high[number]

    def get_bband_pctb_low(self, number: int) -> float:
        return self.bband_pctb_low[number]

    def get_ma_positive_arranged(self, number: int) -> bool:
        return self.ma_positive_arranged[number]

    def get_ma_negative_arranged(self, number: int) -> bool:
        return self.ma_negative_arranged[number]

    def get_rebalance_peridos_index(self) -> list:
        return list(range(len(self.rebalance_periods)))

    def get_momentum_types_index(self) -> list:
        return list(range(len(self.momentum_types)))

    def get_momentum_windows_index(self) -> list:
        return list(self.momentum_windows.keys())

    def get_momentum_select_criteria_index(self) -> list:
        return list(self.momentum_select_criteria.keys())

    def get_momentum_select_counts_index(self) -> list:
        return list(self.momentum_select_counts.keys())

    def get_market_cap_windows_index(self) -> list:
        return list(self.market_cap_windows.keys())

    def get_market_cap_select_criteria_index(self) -> list:
        return list(self.market_cap_select_criteria.keys())

    def get_market_cap_select_counts_index(self) -> list:
        return list(self.market_cap_select_counts.keys())

    def get_volume_windows_index(self) -> list:
        return list(self.volume_windows.keys())

    def get_volume_select_criteria_index(self) -> list:
        return list(self.volume_select_criteria.keys())

    def get_volume_select_counts_index(self) -> list:
        return list(self.volume_select_counts.keys())

    def get_transaction_amount_windows_index(self) -> list:
        return list(self.transaction_amount_windows.keys())

    def get_transaction_amount_select_criteria_index(self) -> list:
        return list(self.transaction_amount_select_criteria.keys())

    def get_transaction_amount_select_counts_index(self) -> list:
        return list(self.transaction_amount_select_counts.keys())

    def get_turn_over_windows_index(self) -> list:
        return list(self.turn_over_windows.keys())

    def get_turn_over_select_criteria_index(self) -> list:
        return list(self.turn_over_select_criteria.keys())

    def get_turn_over_select_counts_index(self) -> list:
        return list(self.turn_over_select_counts.keys())

    def get_absolute_return_windows_index(self) -> list:
        return list(self.absolute_return_windows.keys())

    def get_absolute_return_select_criteria_index(self) -> list:
        return list(self.absolute_return_select_criteria.keys())

    def get_ma5_break_index(self) -> list:
        return list(self.ma5_break.keys())

    def get_ma10_break_index(self) -> list:
        return list(self.ma10_break.keys())

    def get_ma20_break_index(self) -> list:
        return list(self.ma20_break.keys())

    def get_ma60_break_index(self) -> list:
        return list(self.ma60_break.keys())

    def get_ma120_break_index(self) -> list:
        return list(self.ma120_break.keys())

    def get_ma250_break_index(self) -> list:
        return list(self.ma250_break.keys())

    def get_bband_upper_break_index(self) -> list:
        return list(self.bband_upper_break.keys())

    def get_bband_lower_break_index(self) -> list:
        return list(self.bband_lower_break.keys())

    def get_bband_width_high_index(self) -> list:
        return list(self.bband_width_high.keys())

    def get_bband_width_low_index(self) -> list:
        return list(self.bband_width_low.keys())

    def get_bband_pctb_high_index(self) -> list:
        return list(self.bband_pctb_high.keys())

    def get_bband_pctb_low_index(self) -> list:
        return list(self.bband_pctb_low.keys())

    def get_ma_positive_arranged_index(self) -> list:
        return list(self.ma_positive_arranged.keys())

    def get_ma_negative_arranged_index(self) -> list:
        return list(self.ma_negative_arranged.keys())
