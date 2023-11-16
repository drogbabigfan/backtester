import pandas as pd
from data.data_processing.FilterCalculator.utils import Utils


# Momentum Filter 적용 방식
#     - type1: Universe 적용 -> 잔존 종목 중 Momentum 계산
#     - type2 : type1을 loc가 아닌 곱연산으로 적용 -> 상위 n개 선택, 하위 n개 선택
#     - type3 : momentum 적용  -> universe와 곱연산 후 종목수 추출 -> 상위 n개 선택, 하위 n개 선택
#     - type4: Momentum 적용 -> Universe loc 연산 후 종목수 추출 -> 상위 n개 선택, 하위 n개 선택
#     - type5: Momentum 적용 종목수 선택 and universe 적용

class MomentumIndicator:
    def __init__(self):
        self.util = Utils()

    ## TODO: TEST 필요
    def get_type_one_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, up_or_down: str, threshold: float):
        filterd_price = price.loc[universe]
        rank = self.util.calculate_rank(filterd_price)
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    ## TODO: TEST 필요
    def get_type_two_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, up_or_down: str, threshold: float):
        filtered_price = price * universe
        rank = self.util.calculate_rank(filtered_price)
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    ## TODO: TEST 필요
    def get_type_three_momentum(self, universe: pd.DataFrame, price: pd.DataFramem, up_or_down: str, threshold: float):
        filtered_price = self.util.calculate_rank(price)
        rank = filtered_price * universe
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    ## TODO: TEST 필요
    def get_type_four_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, up_or_down: str, threshold: float):
        filtered_price = self.util.calculate_rank(price)
        rank = filtered_price.loc[universe]
        result = self.util.select_logic(rank, up_or_down, threshold)
        return result

    ## TODO: TEST 필요
    def get_type_five_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, up_or_down: str, threshold: float):
        filtered_price = self.util.calculate_rank(price)
        rank = self.util.select_logic(filtered_price, up_or_down, threshold)
        result = rank and universe
        return result

