import bt
import pandas as pd
from backtest.bakctester.momentum_backtest.get_calculated_df import GetCalculatedDf
from backtest.bakctester.momentum_backtest.get_momentum_filter import GetMomentumFilter
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.strategy.strategy_generator import StrategyGenerator


class ParameterDispenser:
    def __init__(self):
        self.momentum_parameters = MomentumParameters()
        self.get_calculated_df = GetCalculatedDf(self.momentum_parameters)
        self.strategy_generator = StrategyGenerator()
        self.momentum_filter = GetMomentumFilter()

    def get_momentum_strategy(self, parameter_dict: dict, price: pd.DataFrame) -> bt.Strategy or None:
        momentum_type_index = parameter_dict['momentum_types']

        if momentum_type_index == 0:
            strategy = self.get_type_one_momentum_strategy(parameter_dict, price)
            return strategy
        elif momentum_type_index == 1:
            strategy = self.get_type_two_momentum_strategy(parameter_dict, price)
            return strategy
        elif momentum_type_index == 2:
            momentum_rank = self.get_calculated_df.get_momentum_rank_df(parameter_dict)
            strategy = self.get_type_three_momentum_strategy(parameter_dict, momentum_rank)
            return strategy
        elif momentum_type_index == 3:
            momentum_rank = self.get_calculated_df.get_momentum_rank_df(parameter_dict)
            strategy = self.get_type_four_momentum_strategy(parameter_dict, momentum_rank)
            return strategy
        elif momentum_type_index == 4:
            momentum_rank = self.get_calculated_df.get_momentum_rank_df(parameter_dict)
            strategy = self.get_type_five_momentum_strategy(parameter_dict, momentum_rank)
            return strategy
        else:
            print('momentum_type_index error : ', momentum_type_index)
            return None

    def get_type_one_momentum_strategy(self, parameter_dict: dict, price: pd.DataFrame) -> bt.Strategy or None:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        window = parameter_dict['momentum_windows']
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        # universe 전부 false면 return None
        if not universe.any().any():
            return None

        # 값으로 넘겨줘야함
        window = self.momentum_parameters.get_momentum_windows(window)
        up_or_down = self.momentum_parameters.get_momentum_select_criteria(up_or_down)
        threshold = self.momentum_parameters.get_momentum_select_counts(threshold)

        select_df = self.momentum_filter.get_type_one_momentum(universe=universe, price=price, window=window,
                                                               up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_two_momentum_strategy(self, parameter_dict: dict, price: pd.DataFrame) -> bt.Strategy or None:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        window = parameter_dict['momentum_windows']
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        # universe dataframe 값이 전부 false면 return None
        if not universe.any().any():
            return None

        # 값으로 넘겨줘야함
        window = self.momentum_parameters.get_momentum_windows(window)
        up_or_down = self.momentum_parameters.get_momentum_select_criteria(up_or_down)
        threshold = self.momentum_parameters.get_momentum_select_counts(threshold)

        select_df = self.momentum_filter.get_type_two_momentum(universe=universe, price=price, window=window,
                                                               up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_three_momentum_strategy(self, parameter_dict: dict, momentum_rank: pd.DataFrame) -> bt.Strategy or None:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        # universe 전부 false면 return None
        if not universe.any().any():
            return None

        # 값으로 넘겨줘야함
        up_or_down = self.momentum_parameters.get_momentum_select_criteria(up_or_down)
        threshold = self.momentum_parameters.get_momentum_select_counts(threshold)

        select_df = self.momentum_filter.get_type_three_momentum(universe=universe, momentum_rank=momentum_rank,
                                                                 up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_four_momentum_strategy(self, parameter_dict: dict, momentum_rank: pd.DataFrame) -> bt.Strategy or None:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        # universe 전부 false면 return None
        if not universe.any().any():
            return None

        # 값으로 넘겨줘야함
        up_or_down = self.momentum_parameters.get_momentum_select_criteria(up_or_down)
        threshold = self.momentum_parameters.get_momentum_select_counts(threshold)

        select_df = self.momentum_filter.get_type_four_momentum(universe=universe, momentum_rank=momentum_rank,
                                                                up_or_down=up_or_down, threshold=threshold)

        strategy_name = self.generate_strategy_name(parameter_dict)
        strategy = self.strategy_generator.get_strategy(strategy_name, select_df)

        return strategy

    def get_type_five_momentum_strategy(self, parameter_dict: dict, momentum_rank: pd.DataFrame) -> bt.Strategy or None:
        universe = self.get_calculated_df.get_universe_df(parameter_dict)
        up_or_down = parameter_dict['momentum_select_criteria']
        threshold = parameter_dict['momentum_select_counts']

        # universe 전부 false면 return None
        if not universe.any().any():
            return None

        # 값으로 넘겨줘야함
        up_or_down = self.momentum_parameters.get_momentum_select_criteria(up_or_down)
        threshold = self.momentum_parameters.get_momentum_select_counts(threshold)

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
