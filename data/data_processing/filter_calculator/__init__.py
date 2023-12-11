from data.data_processing.filter_calculator.market_cap_filter import MarketCapFilter
from data.data_processing.filter_calculator.momentum_filter import MomentumFilter
from data.data_processing.filter_calculator.technical_indicator_filter import TechnicalIndicatorFilter
from data.data_processing.filter_calculator.transaction_filter import TransactionFilter


class FilterCalculator:
    def __init__(self):
        self.market_cap_filter = MarketCapFilter()
        self.momentum_filter = MomentumFilter()
        self.ta_filter = TechnicalIndicatorFilter()
        self.transaction_filter = TransactionFilter()
