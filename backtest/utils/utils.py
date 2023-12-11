import exchange_calendars as xcals
import pandas as pd


class Utils:
    def __init__(self):
        self.calendar = xcals.get_calendar('XKRX')

    def is_week_first_day(self, current_date: pd.Timestamp) -> bool:
        # 주의 첫 영업일 여부 판별 로직
        previous_date = self.calendar.previous_open(current_date)
        previous_week = previous_date.week
        current_week = current_date.week

        return previous_week != current_week

    def is_week_last_day(self, current_date: pd.Timestamp) -> bool:
        # 주의 마지막 영업일 여부 판별 로직
        next_date = self.calendar.next_open(current_date)
        next_week = next_date.week
        current_week = current_date.week

        return next_week != current_week

    def is_month_first_day(self, current_date: pd.Timestamp) -> bool:
        # 월의 첫 영업일 여부 판별 로직
        previous_date = self.calendar.previous_open(current_date)
        previous_month = previous_date.month
        current_month = current_date.month

        return previous_month != current_month

    def is_month_last_day(self, current_date: pd.Timestamp) -> bool:
        # 월의 마지막 영업일 여부 판별 로직
        next_date = self.calendar.next_open(current_date)
        next_month = next_date.month
        current_month = current_date.month

        return next_month != current_month

    def is_quarter_first_day(self, current_date: pd.Timestamp) -> bool:
        # 분기의 첫 영업일 여부 판별 로직
        previous_date = self.calendar.previous_open(current_date)
        previous_quarter = previous_date.quarter
        current_quarter = current_date.quarter

        return previous_quarter != current_quarter

    def is_quarter_last_day(self, current_date: pd.Timestamp) -> bool:
        # 분기의 마지막 영업일 여부 판별 로직
        next_date = self.calendar.next_open(current_date)
        next_quarter = next_date.quarter
        current_quarter = current_date.quarter

        return next_quarter != current_quarter



