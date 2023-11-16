import pandas as pd
import data.data_processing.FilterCalculator.utils as utils


class TransactionFilter:
    def __init__(self):
        self.util = utils.Utils()

    def volume_filter(self, raw_data: pd.DataFrame, period: int, threshold: float):
        if 0 < threshold < 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_high_n_pct(rolling_mean, threshold)
            return result
        elif threshold > 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_high_n_quantity(rolling_mean, threshold)
            return result
        else:
            print("Threshold 값이 이상하므로 확인 필요")

    def transaction_amount_filter(self, raw_data: pd.DataFrame, period: int, threshold: float):
        if 0 < threshold < 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_high_n_pct(rolling_mean, threshold)
            return result
        elif threshold > 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_high_n_quantity(rolling_mean, threshold)
            return result
        else:
            print("Threshold 값이 이상하므로 확인 필요")


    def turn_over_filter(self, raw_data: pd.DataFrame, period: int, threshold: float):
        if 0 < threshold < 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_high_n_pct(rolling_mean, threshold)
            return result
        elif threshold > 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_high_n_quantity(rolling_mean, threshold)
            return result
        else:
            print("Threshold 값이 이상하므로 확인 필요")

