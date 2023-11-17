import pandas as pd


class Utils:
    def __init__(self):
        pass

    def calculate_rank(self, raw_data: pd.DataFrame):
        is_not_nan = raw_data.notnull()
        is_not_zero = raw_data != 0
        raw_data = raw_data[is_not_nan & is_not_zero]
        result = raw_data.rank(axis=1, ascending=False, method='min')
        return result

    # 랭크 내의 상위 n개 추출
    def get_high_n_quantity(self, raw_data: pd.DataFrame, n: float):
        result = self.calculate_rank(raw_data)
        result = result <= n
        return result

    # 랭크 내의 하위 n개 추출
    def get_low_n_quantity(self, raw_data: pd.DataFrame, n: float):
        result = self.calculate_rank(raw_data)
        result = result >= n
        return result

    # 랭크 내의 상위 n% 추출
    def get_high_n_pct(self, raw_data: pd.DataFrame, pct: float):
        result = self.calculate_rank(raw_data)
        result = result.apply(lambda x: x <= x.max() * pct, axis=1)
        # result = result <= max_rank_df * pct
        return result

    # 랭크 내의 하위 n% 추출
    def get_low_n_pct(self, raw_data: pd.DataFrame, pct: float):
        result = self.calculate_rank(raw_data)
        result = result.apply(lambda x: x >= x.max() * pct, axis=1)
        # result = result < max_rank_df * pct
        return result

    def select_up_logic(self, df: pd.DataFrame, threshold: float):
        if 0 < threshold < 1:
            result = self.get_high_n_pct(df, threshold)
            return result
        elif threshold > 1:
            result = self.get_high_n_quantity(df, threshold)
            return result
        else:
            print("Threshold 값이 이상하므로 확인 필요")

    def select_down_logic(self, df: pd.DataFrame, threshold: float):
        if 0 < threshold < 1:
            result = self.get_low_n_pct(df, threshold)
            return result
        elif threshold > 1:
            result = self.get_low_n_quantity(df, threshold)
            return result
        else:
            print("Threshold 값이 이상하므로 확인 필요")

    def select_logic(self, df: pd.DataFrame, up_or_down: str, threshold: float):
        if up_or_down == 'up':
            result = self.select_up_logic(df, threshold)
            return result
        elif up_or_down == 'down':
            result = self.select_down_logic(df, threshold)
            return result
        else:
            print("up_or_down 값이 이상하므로 확인 필요")
