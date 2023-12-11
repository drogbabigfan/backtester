import bt
import pandas as pd
import backtest.strategy.rebalance_condition as rebalance_condition
from backtest.strategy.rebalance_on_condition import RebalanceOnCondition
from backtest.strategy.operation_types import Operation

class StrategyGenerator:
    def __init__(self):
        self.operation = Operation

    def get_strategy(self, strategy_name: str, select_df) -> bt.Strategy:
        rebalance_period = strategy_name.split('_')[0]

        if rebalance_period == 1:
            return self.create_weekly_first_buy_last_sell(strategy_name, select_df)
        elif rebalance_period == 2:
            return self.create_weekly_last_buy_first_sell(strategy_name, select_df)
        elif rebalance_period == 3:
            return self.create_weekly_first_day(strategy_name, select_df)
        elif rebalance_period == 4:
            return self.create_weekly_last_day(strategy_name, select_df)
        elif rebalance_period == 5:
            return self.create_monthly_first_buy_last_sell(strategy_name, select_df)
        elif rebalance_period == 6:
            return self.create_monthly_last_buy_first_sell(strategy_name, select_df)
        elif rebalance_period == 7:
            return self.create_monthly_first_day(strategy_name, select_df)
        elif rebalance_period == 8:
            return self.create_monthly_last_day(strategy_name, select_df)
        elif rebalance_period == 9:
            return self.create_quarterly_first_buy_last_sell(strategy_name, select_df)
        elif rebalance_period == 10:
            return self.create_quarterly_last_buy_first_sell(strategy_name, select_df)
        elif rebalance_period == 11:
            return self.create_quarterly_first_day(strategy_name, select_df)
        elif rebalance_period == 12:
            return self.create_quarterly_last_day(strategy_name, select_df)
        else:
            print("rebalance_period 값이 이상하므로 확인 필요 : ", rebalance_period)

    def create_weekly_first_buy_last_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.WeeklyFirstBuyLastSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy

    def create_weekly_last_buy_first_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.WeeklyLastBuyFirstSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy

    def create_weekly_first_day(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.WeeklyFirstDay()
        operation_condition = RebalanceOnCondition(run_logic, operation=self.operation.REBALANCE)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   operation_condition,
                                   bt.algos.SelectWhere(select_df),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy

    def create_weekly_last_day(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.WeeklyLastDay()
        operation_condition = RebalanceOnCondition(run_logic, operation=self.operation.REBALANCE)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   operation_condition,
                                   bt.algos.SelectWhere(select_df),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy

    def create_monthly_first_buy_last_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.MonthlyFristBuyLastSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy

    def create_monthly_last_buy_first_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.MonthlyLastBuyFirstSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy

    def create_monthly_first_day(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.MonthlyFirstDay()
        operation_condition = RebalanceOnCondition(run_logic, operation=self.operation.REBALANCE)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   operation_condition,
                                   bt.algos.SelectWhere(select_df),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy

    def create_monthly_last_day(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.MonthlyLastDay()
        operation_condition = RebalanceOnCondition(run_logic, operation=self.operation.REBALANCE)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   operation_condition,
                                   bt.algos.SelectWhere(select_df),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy



    def create_quarterly_first_buy_last_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.QuarterlyFristBuyLastSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy

    def create_quarterly_last_buy_first_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.QuarterlyLastBuyFirstSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy

    def create_quarterly_first_day(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.QuarterlyFirstDay()
        operation_condition = RebalanceOnCondition(run_logic, operation=self.operation.REBALANCE)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   operation_condition,
                                   bt.algos.SelectWhere(select_df),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy

    def create_quarterly_last_day(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.QuarterlyLastDay()
        operation_condition = RebalanceOnCondition(run_logic, operation=self.operation.REBALANCE)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   operation_condition,
                                   bt.algos.SelectWhere(select_df),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy


