import pandas as pd

from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from data.data_reader.data_reader import BackTestDataReader


class GetCalculatedDf:
    def __init__(self, momentum_parameter: MomentumParameters):
        self.data_reader = BackTestDataReader()
        self.momentum_parameter = momentum_parameter

    def get_universe_df(self, parameter_dict: dict) -> pd.DataFrame:
        market_cap = self.get_market_cap_filter_df(parameter_dict)
        volume = self.get_volume_filter_df(parameter_dict)
        transaction_amount = self.get_transaction_amount_filter_df(parameter_dict)
        turn_over = self.get_turn_over_filter_df(parameter_dict)
        absolute_return = self.get_absolute_return_filter_df(parameter_dict)
        ma_break = self.get_ma_break_filter_df(parameter_dict)
        bband_break = self.get_bband_break_filter_df(parameter_dict)
        bband_pctb = self.get_bband_pctb_filter_df(parameter_dict)
        bband_width = self.get_bband_width_filter_df(parameter_dict)
        momentum_rank = self.get_momentum_rank_df(parameter_dict)
        ma_arranged = self.get_ma_arranged_filter_df(parameter_dict)

        universe = (market_cap & volume & transaction_amount & turn_over & absolute_return & ma_break & bband_break
                    & bband_pctb & bband_width & momentum_rank & ma_arranged)

        return universe

    def get_market_cap_filter_df(self, parameter_dict: dict) -> pd.DataFrame or bool:
        market_cap_window = parameter_dict['market_cap_windows']
        market_cap_select_criteria = parameter_dict['market_cap_select_criteria']
        market_cap_select_count = parameter_dict['market_cap_select_counts']

        validate = self.check_market_cap_parameter_validate(market_cap_window, market_cap_select_criteria,
                                                            market_cap_select_count)
        if validate:
            return False

        file_name = f"{market_cap_window}_{market_cap_select_criteria}_{market_cap_select_count}"

        # file 읽어서 df 생성
        marcap_df = self.data_reader.get_market_cap_filter_parquet(file_name)

        return marcap_df

    def check_market_cap_parameter_validate(self, market_cap_window: int, market_cap_select_criteria: str,
                                            market_cap_select_count: int) -> bool:
        window_range = self.momentum_parameter.get_market_cap_windows_index()
        criteria_range = self.momentum_parameter.get_market_cap_select_criteria_index()
        count_range = self.momentum_parameter.get_market_cap_select_counts_index()

        not_in_window = market_cap_window not in window_range
        not_in_criteria = market_cap_select_criteria not in criteria_range
        not_in_count = market_cap_select_count not in count_range

        if not_in_window or not_in_criteria or not_in_count:
            return True

    def get_volume_filter_df(self, parameter_dict: dict) -> pd.DataFrame or bool:
        volume_windows = parameter_dict['volume_windows']
        volume_select_counts = parameter_dict['volume_select_counts']
        is_zero = volume_windows == 0 or volume_select_counts == 0

        validate = self.check_volume_parameter_validate(volume_windows, volume_select_counts)

        if validate:
            return False

        if is_zero:
            return True

        file_name = f"{volume_windows}_{volume_select_counts}"

        # file 읽어서 df 생성
        volume_df = self.data_reader.get_volume_filter_parquet(file_name)

        return volume_df

    def check_volume_parameter_validate(self, volume_windows: int, volume_select_counts: int) -> bool:
        window_range = self.momentum_parameter.get_volume_windows_index()
        count_range = self.momentum_parameter.get_volume_select_counts_index()

        not_in_window = volume_windows not in window_range
        not_in_count = volume_select_counts not in count_range

        if not_in_window or not_in_count:
            return True

    def get_transaction_amount_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        transaction_amount_windows = parameter_dict['transaction_amount_windows']
        transaction_amount_select_counts = parameter_dict['transaction_amount_select_counts']
        is_zero = transaction_amount_windows == 0 or transaction_amount_select_counts == 0

        validate = self.check_transaction_amount_parameter_validate(transaction_amount_windows,
                                                                    transaction_amount_select_counts)

        if validate:
            return False

        if is_zero:
            return True

        file_name = f"{transaction_amount_windows}_{transaction_amount_select_counts}"

        # file 읽어서 df 생성
        transaction_amount_df = self.data_reader.get_transaction_amount_filter_parquet(file_name)

        return transaction_amount_df

    def check_transaction_amount_parameter_validate(self, transaction_amount_windows: int,
                                                    transaction_amount_select_counts: int) -> bool:
        window_range = self.momentum_parameter.get_transaction_amount_windows_index()
        count_range = self.momentum_parameter.get_transaction_amount_select_counts_index()

        not_in_window = transaction_amount_windows not in window_range
        not_in_count = transaction_amount_select_counts not in count_range

        if not_in_window or not_in_count:
            return True

    def get_turn_over_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        turn_over_windows = parameter_dict['turn_over_windows']
        turn_over_select_counts = parameter_dict['turn_over_select_counts']
        is_zero = turn_over_windows == 0 or turn_over_select_counts == 0

        validate = self.check_turn_over_parameter_validate(turn_over_windows, turn_over_select_counts)

        if validate:
            return False

        if is_zero:
            return True

        file_name = f"{turn_over_windows}_{turn_over_select_counts}"

        # file 읽어서 df 생성
        turn_over_df = self.data_reader.get_turn_over_filter_parquet(file_name)

        return turn_over_df

    def check_turn_over_parameter_validate(self, turn_over_windows: int, turn_over_select_counts: int) -> bool:
        window_range = self.momentum_parameter.get_turn_over_windows_index()
        count_range = self.momentum_parameter.get_turn_over_select_counts_index()

        not_in_window = turn_over_windows not in window_range
        not_in_count = turn_over_select_counts not in count_range

        if not_in_window or not_in_count:
            return True


    def get_absolute_return_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        absolute_return_windows = parameter_dict['absolute_return_windows']
        absolute_return_select_criteria = parameter_dict['absolute_return_select_criteria']

        if absolute_return_windows == 0:
            return True

        file_name = f"{absolute_return_windows}_{absolute_return_select_criteria}"

        # file 읽어서 df 생성
        absolute_return_df = self.data_reader.get_absolute_return_parquet(file_name)

        return absolute_return_df

    def get_ma_break_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        ma_parms = [5, 10, 20, 60, 120, 250]
        result = True

        for window in ma_parms:
            parm = parameter_dict[f'ma{window}_break']

            if parm == 0:
                continue

            file_name = f"{parm}"

            # file 읽어서 df 생성
            ma_break_df = self.data_reader.get_ma_filter_parquet(window, file_name)
            result = result & ma_break_df

        return result

    def get_bband_break_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        bband_upper_break = parameter_dict['bband_upper_break']
        bband_lower_break = parameter_dict['bband_lower_break']

        # 둘다 0이거나 둘다 0이 아니면 True
        if (bband_upper_break == 0 and bband_lower_break == 0) or (bband_upper_break != 0 and bband_lower_break != 0):
            return True

        if bband_upper_break != 0:
            file_name = f"{bband_upper_break}"
            bband_break = self.data_reader.get_bband_break_filter_parquet('upper', file_name)
            return bband_break
        elif bband_lower_break != 0:
            file_name = f"{bband_lower_break}"
            bband_break = self.data_reader.get_bband_break_filter_parquet('lower', file_name)
            return bband_break

    def get_bband_pctb_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        bband_pctb_high = parameter_dict['bband_pctb_high']
        bband_pctb_low = parameter_dict['bband_pctb_low']

        # 둘다 0이거나 둘다 0이 아니면 True
        if (bband_pctb_high == 0 and bband_pctb_low == 0) or (bband_pctb_high != 0 and bband_pctb_low != 0):
            return True

        if bband_pctb_high != 0:
            file_name = f"{bband_pctb_high}"
            bband_pctb = self.data_reader.get_bband_pctb_filter_parquet('high', file_name)
            return bband_pctb
        elif bband_pctb_low != 0:
            file_name = f"{bband_pctb_low}"
            bband_pctb = self.data_reader.get_bband_pctb_filter_parquet('low', file_name)
            return bband_pctb

    def get_bband_width_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        bband_width_high = parameter_dict['bband_width_high']
        bband_width_low = parameter_dict['bband_width_low']

        # 둘다 0이거나 둘다 0이 아니면 True
        if (bband_width_high == 0 and bband_width_low == 0) or (bband_width_high != 0 and bband_width_low != 0):
            return True

        if bband_width_high != 0:
            file_name = f"{bband_width_high}"
            bband_width = self.data_reader.get_bband_width_filter_parquet('high', file_name)
            return bband_width
        elif bband_width_low != 0:
            file_name = f"{bband_width_low}"
            bband_width = self.data_reader.get_bband_width_filter_parquet('low', file_name)
            return bband_width

    def get_momentum_rank_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        momentum_windows = parameter_dict['momentum_windows']

        if momentum_windows == 0:
            return True

        file_name = f"{momentum_windows}"

        momentum_rank_df = self.data_reader.get_calculated_momentum_rank_parquet(file_name)
        return momentum_rank_df

    def get_ma_arranged_filter_df(self, parameter_dict: dict) -> pd.DataFrame or True:
        positive = parameter_dict['ma_positive_arranged']
        negative = parameter_dict['ma_negative_arranged']

        if (positive == 1 and negative == 1) or (positive == 0 and negative == 0):
            return True

        if positive == 1:
            file_name = f"{positive}"
            ma_arranged_df = self.data_reader.get_ma_positive_arranged_filter_parquet(file_name)
            return ma_arranged_df
        elif negative == 1:
            file_name = f"{negative}"
            ma_arranged_df = self.data_reader.get_ma_negative_arranged_filter_parquet(file_name)
            return ma_arranged_df
