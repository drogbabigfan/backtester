from unittest import TestCase

import bt
import pandas as pd

from backtest.strategy_generator import StrategyGenerator
from data.data_processing.data_handler import DataHandler
from data.data_processing.FilterCalculator.market_cap_filter import MarketCapFilter
from data.data_processing.FilterCalculator.momentum_filter import MomentumFilter
from data.data_processing.FilterCalculator.technical_indicator_filter import TechnicalIndicatorFilter
from data.data_processing.FilterCalculator.transaction_filter import TransactionFilter


class TestStrategyGenerator(TestCase):
    def setUp(self):
        self.test_data = self.get_test_data()
        self.strategy_generator = StrategyGenerator()

    def test_create_weekly_first_buy_last_sell(self):
        marcap_filter = self.get_market_cap_filter()
        transaction_filter = self.get_transaction_filter()
        universe = marcap_filter & transaction_filter

        momentum_filter = self.get_momnentum_filter(universe)
        # momentum_filter = self.get_momnentum_filter(marcap_filter)
        ta_filter = self.get_ta_filter()

        # select_df = marcap_filter & momentum_filter & transaction_filter & ta_filter
        select_df = momentum_filter & ta_filter

        strategy = self.strategy_generator.create_weekly_first_buy_last_sell("test", select_df=select_df)

        test = bt.Backtest(strategy, self.test_data)
        result = bt.run(test)

        result.plot()
        result.display()

        transaction = result.get_transactions()
        print("transaction : ", transaction)

        trade_count = len(transaction)
        print("trade_count : ", trade_count)

        traded_securities = transaction.index.get_level_values('Security').unique()
        print("traded_securities : ", traded_securities)

    def get_market_cap_filter(self) -> pd.DataFrame:
        market_cap_filter = MarketCapFilter()
        result = market_cap_filter.get_large_market_cap_filter(self.test_data, 60, 0.2)
        return result

    def get_momnentum_filter(self, universe: pd.DataFrame) -> pd.DataFrame:
        momentum_filter = MomentumFilter()
        reuslt = momentum_filter.get_type_one_momentum(universe=universe, price=self.test_data, window=60,
                                                       up_or_down="up", threshold=30)
        return reuslt

    def get_transaction_filter(self) -> pd.DataFrame:
        transaction_filter = TransactionFilter()
        result = transaction_filter.volume_filter(self.test_data, 20, 0.1)
        return result

    def get_ta_filter(self) -> pd.DataFrame:
        ta_filter = TechnicalIndicatorFilter()
        result = ta_filter.get_ma_upper_breakout(self.test_data, 20)
        return result

    def get_test_data(self):
        data_handler = DataHandler()
        raw_data = data_handler.get_csv_raw_data("all_marcap.csv") / 100_000_000
        clean_data = data_handler.process_nan_to_zero(raw_data)
        return clean_data