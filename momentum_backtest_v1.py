from backtest.bakctester.momentum_backtest.momentum_strategy_backtester import MomentumStrategyBacktester
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder
from optimization.genetic_algorithm.genetic_algorithm_optimizer import GeneticAlgorithmOptimizer


class MomentumBacktestV1:
    def __init__(self):
        self.momentum_parameter = MomentumParameters()
        self.parameter_encoder = ParameterEncoderDecoder(self.momentum_parameter)
        self.momentum_backtest = MomentumStrategyBacktester(momentum_parameter=self.momentum_parameter,
                                                            parameter_encoder=self.parameter_encoder)
        self.genetic_algorithm = GeneticAlgorithmOptimizer(parameter_encoder=self.parameter_encoder,
                                                           backtest_simulator=self.momentum_backtest)

    def run(self):
        num_parameters = self.momentum_parameter.get_number_of_parameters()
        parameter_dict = self.momentum_parameter.get_parameter_dict()

        optimal_params, optimal_fitness = self.genetic_algorithm.run(num_parameters=num_parameters,
                                                                     num_agents=100000,
                                                                     max_iter=10,
                                                                     parameter_dict=parameter_dict)
        print(optimal_params)
        print(optimal_fitness)


if __name__ == '__main__':
    MomentumBacktestV1().run()
