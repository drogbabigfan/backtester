import pandas as pd
from data.data_processing.FilterCalculator.utils import Utils


# Momentum Filter 적용 방식
#     - type1: Universe 적용 -> 잔존 종목 중 Momentum 계산
#     - type2 : type1을 loc가 아닌 곱연산으로 적용 -> 상위 n개 선택, 하위 n개 선택
#     - type3 : momentum 적용  -> universe와 곱연산 후 종목수 추출 -> 상위 n개 선택, 하위 n개 선택
#     - type4: Momentum 적용 -> Universe loc 연산 후 종목수 추출 -> 상위 n개 선택, 하위 n개 선택
#     - type5: Momentum 적용 종목수 선택 and universe 적용

class MomentumFilter:
    def __init__(self):
        self.util = Utils()

    def calculate_period_return(self, raw_data: pd.DataFrame, window: int):
        result = (raw_data / raw_data.shift(window) - 1) * 100
        return result

    def get_type_one_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, window: int, up_or_down: str,
                              threshold: float):
        filterd_price = price[universe]
        momentum = self.calculate_period_return(filterd_price, window)
        rank = self.util.calculate_rank(momentum)
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    def get_type_two_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, window: int, up_or_down: str,
                              threshold: float):
        filtered_price = price * universe
        momentum = self.calculate_period_return(filtered_price, window)
        rank = self.util.calculate_rank(momentum)
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    def get_type_three_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, window: int, up_or_down: str,
                                threshold: float):
        momentum = self.calculate_period_return(price, window)
        momentum_rank = self.util.calculate_rank(momentum)
        rank = momentum_rank * universe
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    def get_type_four_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, window: int, up_or_down: str,
                               threshold: float):
        momentum = self.calculate_period_return(price, window)
        momentum_rank = self.util.calculate_rank(momentum)
        rank = momentum_rank[universe]
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    def get_type_five_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, widnow: int, up_or_down: str, threshold: float):
        momentum = self.calculate_period_return(price, widnow)
        momentum_rank = self.util.calculate_rank(momentum)
        rank = self.util.select_logic(momentum_rank, up_or_down, threshold)
        result = rank & universe
        return result

    def get_calculate_return_plus(self, raw_data: pd.DataFrame, window: int):
        result = self.calculate_period_return(raw_data, window)
        result = result > 0
        return result

    def get_calculate_return_minus(self, raw_data: pd.DataFrame, window: int):
        result = self.calculate_period_return(raw_data, window)
        result = result < 0
        return result
