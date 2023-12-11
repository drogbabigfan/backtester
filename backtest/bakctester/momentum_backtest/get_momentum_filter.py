import pandas as pd
from data.data_processing.filter_calculator import MomentumFilter


class GetMomentumFilter:
    def __init__(self):
        self.momentum_filter = MomentumFilter()

    def get_type_one_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, window: int, up_or_down: str,
                              threshold: float):
        return self.momentum_filter.get_type_one_momentum(universe=universe, price=price, window=window,
                                                          up_or_down=up_or_down, threshold=threshold)

    def get_type_two_momentum(self, universe: pd.DataFrame, price: pd.DataFrame, window: int, up_or_down: str,
                              threshold: float):
        return self.momentum_filter.get_type_two_momentum(universe=universe, price=price, window=window,
                                                          up_or_down=up_or_down, threshold=threshold)

    def get_type_three_momentum(self, universe: pd.DataFrame, momentum_rank: pd.DataFrame, up_or_down: str,
                                threshold: float):
        rank = momentum_rank * universe
        result = self.momentum_filter.util.select_logic(rank, up_or_down, threshold)
        return result

    def get_type_four_momentum(self, universe: pd.DataFrame, momentum_rank: pd.DataFrame, up_or_down: str,
                               threshold: float):
        rank = momentum_rank[universe]
        result = self.momentum_filter.util.select_logic(rank, up_or_down, threshold)
        return result

    def get_type_five_momentum(self, universe: pd.DataFrame, momentum_rank: pd.DataFrame, up_or_down: str,
                               threshold: float):
        rank = self.momentum_filter.util.select_logic(momentum_rank, up_or_down, threshold)
        result = rank & universe
        return result
