import abc
import pandas as pd

class BacktesterForOptimization(abc.ABC):

    @abc.abstractmethod
    def run_backtest(self, parameter_list: list):
        pass

    @abc.abstractmethod
    def evaluation(self, *args):
        pass

    @abc.abstractmethod
    def save_backtest_result(self, strategy_name:str, backtest_result: pd.DataFrame):
        pass

