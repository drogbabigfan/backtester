from data.data_processing.FilterCalculator.utils import Utils
import pandas as pd


class MarketCapFilter:
    def __init__(self):
        self.util = Utils()

    def get_large_market_cap_filter(self, raw_data: pd.DataFrame, period: int, threshold: float):
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

    def get_small_market_cap_filter(self, raw_data: pd.DataFrame, period: int, threshold: float):
        if 0 < threshold < 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_low_n_pct(rolling_mean, threshold)
            return result
        elif threshold > 1:
            rolling_mean = raw_data.rolling(window=period).mean()
            result = self.util.get_low_n_quantity(rolling_mean, threshold)
            return result
        else:
            print("Threshold 값이 이상하므로 확인 필요")
