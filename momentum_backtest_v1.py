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

    def run(self):
        num_parameters = self.momentum_parameter.get_number_of_parameters()
        parameter_dict = self.momentum_parameter.get_parameter_dict()

        optimizer = GeneticAlgorithmOptimizer(num_agents=5, num_parameters=num_parameters,
                                              parameter_dict=parameter_dict,
                                              num_generations=10,
                                              num_parents_mating=2,
                                            backtest_simulator=self.momentum_backtest)

        best_solution, best_solution_fitness = optimizer.run()

        print(best_solution)
        print(best_solution_fitness)





if __name__ == '__main__':
    MomentumBacktestV1().run()
