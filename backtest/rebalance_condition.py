from abc import ABC, abstractmethod
import exchange_calendars as xcals
import pandas as pd
import backtest.utils as utils


class RebalanceCondition(ABC):
    def __init__(self):
        self.utils = utils.Utils()

    @abstractmethod
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        pass


class WeeklyFirstBuyLastSell(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == 'buy':
            return self.utils.is_week_first_day(current_date)
        elif operation == 'sell':
            return self.utils.is_week_last_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class WeeklyLastBuyFirstSell(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == 'buy':
            return self.utils.is_week_last_day(current_date)
        elif operation == 'sell':
            return self.utils.is_week_first_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class WeeklyFirstDay(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == "rebalance":
            return self.utils.is_week_first_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class WeeklyLastDay(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == "rebalance":
            return self.utils.is_week_last_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class MonthlyFristBuyLastSell(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == 'buy':
            return self.utils.is_month_first_day(current_date)
        elif operation == 'sell':
            return self.utils.is_month_last_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class MonthlyLastBuyFirstSell(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == 'buy':
            return self.utils.is_month_last_day(current_date)
        elif operation == 'sell':
            return self.utils.is_month_first_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class MonthlyFirstDay(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == "rebalance":
            return self.utils.is_month_first_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class MonthlyLastDay(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == "rebalance":
            return self.utils.is_month_last_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class QuarterlyFirstBuyLastSell(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == 'buy':
            return self.utils.is_quarter_first_day(current_date)
        elif operation == 'sell':
            return self.utils.is_quarter_last_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class QuarterlyLastBuyFirstSell(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == 'buy':
            return self.utils.is_quarter_last_day(current_date)
        elif operation == 'sell':
            return self.utils.is_quarter_first_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class QuarterlyFirstDay(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == "rebalance":
            return self.utils.is_quarter_first_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")


class QuarterlyLastDay(RebalanceCondition):
    def check_rebalance_condition(self, current_date: pd.Timestamp, operation: str) -> bool:
        if operation == "rebalance":
            return self.utils.is_quarter_last_day(current_date)
        else:
            print("operation 값이 이상하므로 확인 필요")
