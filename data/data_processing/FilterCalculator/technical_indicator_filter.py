import logging

import pandas as pd

class TechnicalIndicatorFilter:

    def calculate_moving_average(self, raw_data: pd.DataFrame, window: int):
        if len(raw_data) < window:
            logging.log(logging.ERROR, "window size is bigger than raw data size")
        return raw_data.rolling(window=window).mean()

    def calculate_standard_deviation(self, data: pd.DataFrame, window: int):
        if len(data) < window:
            logging.log(logging.ERROR, "window size is bigger than raw data size")
        return data.rolling(window=window).std()

    def calculate_ma_disparity(self, raw_data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(raw_data, window)
        result = raw_data / ma * 100
        return result

    def calculate_upper_bollinger_band(self, data: pd.DataFrame, window: int, multiple: float):
        ma = self.calculate_moving_average(data, window)
        std = self.calculate_standard_deviation(data, window)
        return ma + std * multiple

    def calculate_lower_bollinger_band(self, data: pd.DataFrame, window: int, multiple:float):
        ma = self.calculate_moving_average(data, window)
        std = self.calculate_standard_deviation(data, window)
        return ma - std * multiple

    def calculate_bollinger_band_width(self, raw_data: pd.DataFrame, window: int, multiple:float):
        upper = self.calculate_upper_bollinger_band(raw_data, window, multiple)
        lower = self.calculate_lower_bollinger_band(raw_data, window, multiple)
        middle = self.calculate_moving_average(raw_data, window)
        result = (upper - lower) / middle * 100
        return result

    def calculate_bollinger_band_pctb(self, raw_data: pd.DataFrame, window: int, multiple:float):
        upper = self.calculate_upper_bollinger_band(raw_data, window, multiple)
        lower = self.calculate_lower_bollinger_band(raw_data, window, multiple)
        result = (raw_data - lower) / (upper - lower) * 100
        return result

    def get_ma_upper_breakout(self, raw_data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(raw_data, window)
        result = raw_data > ma
        return result

    def get_ma_lower_breakout(self, raw_data: pd.DataFrame, window: int):
        ma = self.calculate_moving_average(raw_data, window)
        result = raw_data < ma
        return result

    def get_bollinger_band_upper_breakout(self, raw_data: pd.DataFrame, window: int, multiple: float):
        upper = self.calculate_upper_bollinger_band(raw_data, window, multiple)
        result = raw_data > upper
        return result

    def get_bollinger_band_lower_breakout(self, raw_data: pd.DataFrame, window: int, multiple: float):
        lower = self.calculate_lower_bollinger_band(raw_data, window, multiple)
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

    def is_bollinger_band_width_high(self, raw_data: pd.DataFrame, window: int, pct: float, multiple: float):
        bollinger_band_width = self.calculate_bollinger_band_width(raw_data, window, multiple)
        result = bollinger_band_width > pct
        return result

    def is_bollinger_band_width_low(self, raw_data: pd.DataFrame, window: int, pct: float, multiple: float):
        bollinger_band_width = self.calculate_bollinger_band_width(raw_data, window, multiple)
        result = bollinger_band_width < pct
        return result

    def is_bollinger_band_pctb_high(self, raw_data: pd.DataFrame, window: int, pct: float, multiple: float):
        bollinger_band_pctb = self.calculate_bollinger_band_pctb(raw_data, window, multiple)
        result = bollinger_band_pctb > pct
        return result

    def is_bollinger_band_pctb_low(self, raw_data: pd.DataFrame, window: int, pct: float, multiple: float):
        bollinger_band_pctb = self.calculate_bollinger_band_pctb(raw_data, window, multiple)
        result = bollinger_band_pctb < pct
        return result

    ## 이평선 정배열인 경우 ma5 > ma20 > ma60
    def is_ma_positive_arranged(self, raw_data: pd.DataFrame):
        ma5 = self.calculate_moving_average(raw_data, 5)
        ma20 = self.calculate_moving_average(raw_data, 20)
        ma60 = self.calculate_moving_average(raw_data, 60)
        result = (ma5 > ma20) & (ma20 > ma60)
        return result

    ## 이평선 역배열인 경우 ma5 < ma20 < ma60
    def is_ma_negative_arranged(self, raw_data: pd.DataFrame):
        ma5 = self.calculate_moving_average(raw_data, 5)
        ma20 = self.calculate_moving_average(raw_data, 20)
        ma60 = self.calculate_moving_average(raw_data, 60)
        result = (ma5 < ma20) & (ma20 < ma60)
        return result