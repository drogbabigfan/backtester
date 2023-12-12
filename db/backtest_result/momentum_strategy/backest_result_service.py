import pandas as pd
from peewee import *

from db.backtest_result.momentum_strategy.backtest_result_handler import BacktestResultHandler


class BacktestResultService:
    def __init__(self):
        self.db = MySQLDatabase('momentum_backtest', host='localhost', port=3306, user='root', password='1234')
        self.handler = BacktestResultHandler(self.db)
        self.init_table()

    def init_table(self):
        is_exist = self.handler.check_table_exist()

        if not is_exist:
            self.handler.init_table()


    def get_backtest_result_by_strategy_name(self, strategy_name: str):
        return self.handler.get_backtest_result_by_strategy_name(strategy_name=strategy_name)

    def upload_backtest_result(self, strategy_name: str, backtest_result: pd.DataFrame):
        db_result = self.handler.get_backtest_result_by_strategy_name(strategy_name)

        total_return = backtest_result['total_return']
        daily_sharp = backtest_result['daily_sharpe']
        daily_sortino = backtest_result['daily_sortino']
        cagr = backtest_result['cagr']
        max_drawdonw = backtest_result['max_drawdown']
        calmar_ratio = backtest_result['calmar_ratio']
        best_day = backtest_result['best_day']
        worst_day = backtest_result['worst_day']
        best_month = backtest_result['best_month']
        worst_month = backtest_result['worst_month']
        best_year = backtest_result['best_year']
        worst_year = backtest_result['worst_year']
        avg_drawdown = backtest_result['avg_drawdown']
        avg_drawdown_days = backtest_result['avg_drawdown_days']
        avg_up_month = backtest_result['avg_up_month']
        avg_down_month = backtest_result['avg_down_month']
        win_year_rate = backtest_result['win_year_perc']

        if len(db_result) > 0:
            self.handler.update_backtest_result(
                strategy_name=strategy_name,
                total_return=total_return,
                daily_sharp=daily_sharp,
                daily_sortino=daily_sortino,
                cagr=cagr,
                mdd=max_drawdonw,
                calmar_ratio=calmar_ratio,
                best_day=best_day,
                worst_day=worst_day,
                best_month=best_month,
                worst_month=worst_month,
                best_year=best_year,
                worst_year=worst_year,
                avg_drawdown=avg_drawdown,
                avg_drawdown_days=avg_drawdown_days,
                avg_up_month=avg_up_month,
                avg_down_month=avg_down_month,
                win_year_rate=win_year_rate
            )

        else:
            self.handler.add_new_backtest_result(
                strategy_name=strategy_name,
                total_return=total_return,
                daily_sharp=daily_sharp,
                daily_sortino=daily_sortino,
                cagr=cagr,
                mdd=max_drawdonw,
                calmar_ratio=calmar_ratio,
                best_day=best_day,
                worst_day=worst_day,
                best_month=best_month,
                worst_month=worst_month,
                best_year=best_year,
                worst_year=worst_year,
                avg_drawdown=avg_drawdown,
                avg_drawdown_days=avg_drawdown_days,
                avg_up_month=avg_up_month,
                avg_down_month=avg_down_month,
                win_year_rate=win_year_rate
            )
