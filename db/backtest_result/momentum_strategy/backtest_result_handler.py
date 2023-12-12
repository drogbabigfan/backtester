from peewee import *


class BacktestResultHandler:
    def __init__(self, db):
        self.db = db

        class BacktestResult(Model):
            strategy_name = CharField()
            total_return = FloatField()
            daily_sharp = FloatField()
            daily_sortino = FloatField()
            cagr = FloatField()
            mdd = FloatField()
            calmar_ratio = FloatField()
            best_day = FloatField()
            worst_day = FloatField()
            best_month = FloatField()
            worst_month = FloatField()
            best_year = FloatField()
            worst_year = FloatField()
            avg_drawdown = FloatField()
            avg_drawdown_days = FloatField()
            avg_up_month = FloatField()
            avg_down_month = FloatField()
            win_year_rate = FloatField()

            class Meta:
                database = self.db
                table_name = 'backtest_result'

        self.BacktestResultTable = BacktestResult

    def check_db_connect(self, db):
        if db.is_closed():
            db.connect()

    def init_table(self):
        self.db.create_tables([self.BacktestResultTable])

    def check_table_exist(self):
        with self.db:
            return self.db.table_exists(self.BacktestResultTable)

    def get_backtest_result_by_strategy_name(self, strategy_name):
        query = self.BacktestResultTable.select().where(self.BacktestResultTable.strategy_name == strategy_name)
        backtest_result = query.execute()

        return backtest_result

    def add_new_backtest_result(self, strategy_name: str, total_return: float, daily_sharp: float, daily_sortino: float,
                                cagr: float, mdd: float, calmar_ratio: float, best_day: float, worst_day: float,
                                best_month: float, worst_month: float, best_year: float, worst_year: float,
                                avg_drawdown: float, avg_drawdown_days: float, avg_up_month: float,
                                avg_down_month: float, win_year_rate: float):

        self.BacktestResultTable.create(
            strategy_name=strategy_name,
            total_return=total_return,
            daily_sharp=daily_sharp,
            daily_sortino=daily_sortino,
            cagr=cagr,
            mdd=mdd,
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

    def update_backtest_result(self, strategy_name: str, total_return: float, daily_sharp: float, daily_sortino: float,
                                cagr: float, mdd: float, calmar_ratio: float, best_day: float, worst_day: float,
                                best_month: float, worst_month: float, best_year: float, worst_year: float,
                                avg_drawdown: float, avg_drawdown_days: float, avg_up_month: float,
                                avg_down_month: float, win_year_rate: float):

        query = self.BacktestResultTable.update(
            total_return=total_return,
            daily_sharp=daily_sharp,
            daily_sortino=daily_sortino,
            cagr=cagr,
            mdd=mdd,
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
        ).where(self.BacktestResultTable.strategy_name == strategy_name)
        query.execute()