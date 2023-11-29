import bt
import pandas as pd
import backtest.rebalance_condition as rebalance_condition
from backtest.rebalance_on_condition import RebalanceOnCondition
from backtest.operation_types import Operation


class StrategyGenerator:
    def __init__(self):
        self.operation = Operation

    def create_weekly_first_buy_last_sell(self, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.WeeklyFirstBuyLastSell()
        buy_condition = RebalanceOnCondition(run_logic, operation=self.operation.BUY)
        sell_condition = RebalanceOnCondition(run_logic, operation=self.operation.SELL)

        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   # bt.algos.RunMonthly(),
                                   bt.algos.SelectWhere(select_df),
                                   buy_condition,
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                                   sell_condition
                               ])
        return strategy


