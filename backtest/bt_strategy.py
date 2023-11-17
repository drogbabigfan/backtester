import bt
import pandas as pd
import backtest.rebalance_condition as rebalance_condition

class DynamicBacktestStrategy:
    def __init__(self):
        pass

    ## TODO: Test 필요
    def create_weekly_first_buy_last_sell(data: pd.DataFrame, startegy_name: str, select_df: pd.DataFrame):
        run_logic = rebalance_condition.WeeklyFirstBuyLastSell()
        strategy = bt.Strategy(name=startegy_name,
                               algos=[
                                   bt.algos.SelectWhere(select_df),

                                   run_logic.check_rebalance_condition('buy'),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),

                                   run_logic.check_rebalance_condition('sell'),
                                   bt.algos.WeighEqually(),
                                   bt.algos.Rebalance(),
                               ])
        return strategy

