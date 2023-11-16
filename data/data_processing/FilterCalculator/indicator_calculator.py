import os
import pandas as pd


# TODO: Momentum Indcator, Size Indicator, TechnicalIndicator 분류해줘야함

class IndicatorCalculator:
    def __init__(self):
        self.csv_path = os.path.dirname(os.path.abspath(__file__)) + '/../data_collector/csv'
        self.parquet_path = os.path.dirname(os.path.abspath(__file__)) + '/../data_collector/parquet'

    def get_raw_data(self, file_name: str):
        raw_data_path = self.csv_path + f"/raw_data/{file_name}"

        if os.path.isfile(raw_data_path):
            raw_data = pd.read_csv(raw_data_path, index_col=0, header=0, encoding='utf-8-sig', dtype=str)
            columns = raw_data.columns.astype(str)
            raw_data.columns = columns
            raw_data = raw_data.astype(float)
            return raw_data
        else:
            print(f"{file_name} does not exist.")

    def calculate_moving_average(self, raw_data: pd.DataFrame, window: int):
        return raw_data.rolling(window=window).mean()

    def calculate_standard_deviation(self, data: pd.DataFrame, window: int):
        return data.rolling(window=window).std()

    def calculate_ma_disparity(self, raw_data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(raw_data, window)
        result = raw_data / ma * 100
        return result

    def calculate_period_return(self, raw_data: pd.DataFrame, window: int):
        result = (raw_data / raw_data.shift(window) - 1) * 100
        return result
        # 공통 계산 로직: 표준 편차 계산

    def calculate_upper_bollinger_band(self, data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(data, window)
        std = self.calculate_standard_deviation(data, window)
        return ma + std * 2

    def calculate_lower_bollinger_band(self, data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(data, window)
        std = self.calculate_standard_deviation(data, window)
        return ma - std * 2

    def calculate_bollinger_band_width(self, raw_data: pd.DataFrame, window: int):
        upper = self.calculate_upper_bollinger_band(raw_data, window)
        lower = self.calculate_lower_bollinger_band(raw_data, window)
        result = (upper - lower) / raw_data * 100
        return result

    def get_calculate_return_plus(self, raw_data: pd.DataFrame, window: int):
        result = self.calculate_period_return(raw_data, window)
        result = result > 0
        return result

    def get_calculate_return_minus(self, raw_data: pd.DataFrame, window: int):
        result = self.calculate_period_return(raw_data, window)
        result = result < 0
        return result

    def get_momentum_rank_high_percentage(self, raw_data: pd.DataFrame, window: int, pct: float):
        result = self.calculate_period_return(raw_data, window)
        result = self.calculate_rank(result)
        max_rank = result.max(axis=1)
        result = result > max_rank * pct
        return result

    def get_momentum_rank_low_percentage(self, raw_data: pd.DataFrame, window: int, pct: float):
        result = self.calculate_period_return(raw_data, window)
        result = self.calculate_rank(result)
        max_rank = result.max(axis=1)
        result = result < max_rank * pct
        return result

    def get_momentum_high_n_quantity(self, raw_data: pd.DataFrame, window: int, n: int):
        result = self.calculate_period_return(raw_data, window)
        result = self.calculate_rank(result)
        result = result <= n
        return result

    def get_momentum_low_n_quantity(self, raw_data: pd.DataFrame, window: int, n: int):
        result = self.calculate_period_return(raw_data, window)
        result = self.calculate_rank(result)
        result = result >= n
        return result

    def get_marcap_size_high_percentage(self, raw_data: pd.DataFrame, window: int, pct: float):
        result = raw_data.rolling(window=window).mean()
        result = self.calculate_rank(result)
        max_rank = result.max(axis=1)
        result = result > max_rank * pct
        return result

    def get_marcap_size_low_percentage(self, raw_data: pd.DataFrame, window: int, pct: float):
        result = raw_data.rolling(window=window).mean()
        result = self.calculate_rank(result)
        max_rank = result.max(axis=1)
        result = result < max_rank * pct
        return result

    def get_marcap_size_high_n_quantity(self, raw_data: pd.DataFrame, window: int, n: int):
        result = raw_data.rolling(window=window).mean()
        result = self.calculate_rank(result)
        result = result <= n
        return result

    def get_marcap_size_low_n_quantity(self, raw_data: pd.DataFrame, window: int, n: int):
        result = raw_data.rolling(window=window).mean()
        result = self.calculate_rank(result)
        result = result >= n
        return result

    def get_ma_upper_breakout(self, raw_data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(raw_data, window)
        result = raw_data > ma
        return result

    def get_ma_lower_breakout(self, raw_data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(raw_data, window)
        result = raw_data < ma
        return result

    def get_bollinger_band_upper_breakout(self, raw_data: pd.DataFrame, window: int):
        upper = self.calculate_upper_bollinger_band(raw_data, window)
        result = raw_data > upper
        return result

    def get_bollinger_band_lower_breakout(self, raw_data: pd.DataFrame, window: int):
        lower = self.calculate_lower_bollinger_band(raw_data, window)
        result = raw_data < lower
        return result

    def is_disparity_high(self, raw_data: pd.DataFrame, window: int, pct: float):
        disparity = self.calculate_ma_disparity(raw_data, window)
        result = disparity > pct
        return result

    def is_disparity_low(self, raw_data: pd.DataFrame, window: int, pct: float):
        disparity = self.calculate_ma_disparity(raw_data, window)
        result = disparity < pct
        return result

    def is_bollinger_band_width_high(self, raw_data: pd.DataFrame, window: int, pct: float):
        bollinger_band_width = self.calculate_bollinger_band_width(raw_data, window)
        result = bollinger_band_width > pct
        return result

    def is_bollinger_band_width_low(self, raw_data: pd.DataFrame, window: int, pct: float):
        bollinger_band_width = self.calculate_bollinger_band_width(raw_data, window)
        result = bollinger_band_width < pct
        return result

    def calculate_rank(self, raw_data: pd.DataFrame):
        # 0이거나 nan값인 경우 rank 계산에서 제외
        is_not_nan = raw_data.notnull()
        is_not_zero = raw_data != 0
        raw_data = raw_data[is_not_nan & is_not_zero]
        result = raw_data.rank(axis=1, ascending=False, method='min')
        return result
