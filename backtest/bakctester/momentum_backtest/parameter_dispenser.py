import bt
import pandas as pd
from backtest.bakctester.momentum_backtest.get_calculated_df import GetCalculatedDf
from backtest.bakctester.momentum_backtest.get_momentum_filter import GetMomentumFilter
from backtest.strategy.strategy_generator import StrategyGenerator


class ParameterDispenser:
    def __init__(self):
        self.get_calculated_df = GetCalculatedDf()
        self.strategy_generator = StrategyGenerator()
        self.momentum_filter = GetMomentumFilter()


    def get_momentum_strategy(self, parameter_dict: dict, price: pd.DataFrame) -> bt.Strategy:
        momentum_type = parameter_dict['momentum_types']

        if momentum_type == 1:
            strategy = self.get_type_one_momentum_strategy(parameter_dict, price)
        elif momentum_type == 2:
            strategy = self.get_type_two_momentum_strategy(parameter_dict, price)
        elif momentum_type == 3:
            momentum_rank = self.get_calculated_df.get_momentum_rank_df(parameter_dict)
            strategy = self.get_type_three_momentum_strategy(parameter_dict, momentum_rank)
        elif momentum_type == 4:
            momentum_rank = self.get_calculated_df.get_momentum_rank_df(parameter_dict)
            strategy = self.get_type_four_momentum_strategy(parameter_dict, momentum_rank)
        elif momentum_type == 5:
            momentum_rank = self.get_calculated_df.get_momentum_rank_df(parameter_dict)
            strategy = self.get_type_five_momentum_strategy(parameter_dict, momentum_rank)
        else:
            print('momentum_type error : ', momentum_type)
            return 0

    def get_type_one_momentum_strategy(self, parameter_dict: dict, price: pd.DataFrame) -> bt.Strategy:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        window = parameter_dict['momentum_windows']
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        select_df = self.momentum_filter.get_type_one_momentum(universe=universe, price=price, window=window,
                                                               up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_two_momentum_strategy(self, parameter_dict: dict, price: pd.DataFrame) -> bt.Strategy:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        window = parameter_dict['momentum_windows']
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        select_df = self.momentum_filter.get_type_two_momentum(universe=universe, price=price, window=window,
                                                               up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_three_momentum_strategy(self, parameter_dict: dict, momentum_rank: pd.DataFrame) -> bt.Strategy:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        select_df = self.momentum_filter.get_type_three_momentum(universe=universe, momentum_rank=momentum_rank,
                                                                 up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_four_momentum_strategy(self, parameter_dict: dict, momentum_rank: pd.DataFrame) -> bt.Strategy:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        select_df = self.momentum_filter.get_type_four_momentum(universe=universe, momentum_rank=momentum_rank,
                                                                up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_five_momentum_strategy(self, parameter_dict: dict, momentum_rank: pd.DataFrame) -> bt.Strategy:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        select_df = self.momentum_filter.get_type_five_momentum(universe=universe, momentum_rank=momentum_rank,
                                                                up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def generate_strategy_name(self, parameter_dict: dict):
        strategy_name = ''
        for key, value in parameter_dict.items():
            strategy_name += f"{value}_"
        return strategy_name[:-1]
