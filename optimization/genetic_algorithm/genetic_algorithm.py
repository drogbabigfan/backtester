import bt.backtest

from backtest.bakctester.backtester_for_optimization import BacktesterForOptimization


class GeneticAlgorithmForMomentumStrategy:
    def __init__(self, backtest_simulator: BacktesterForOptimization):
        self.backtest_simulator = backtest_simulator

    def fitness_wrapper(self, encoded_params, *args):
        return self.backtest_simulator.evaluation(encoded_params)
