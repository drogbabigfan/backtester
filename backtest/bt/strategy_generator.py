import bt
import pandas as pd
import backtest.bt.rebalance_condition as rebalance_condition
from backtest.bt.rebalance_on_condition import RebalanceOnCondition
from backtest.bt.operation_types import Operation


class StrategyGenerator:
    def __init__(self):
        self.operation = Operation

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

