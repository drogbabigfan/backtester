from Py_FS.wrapper.nature_inspired import GA
import numpy as np

class GeneticAlgorithmOptimizer:
    def __init__(self, encoder, backtest_simulator):
        self.encoder = encoder
        self.backtest_simulator = backtest_simulator

    def run(self):
        # 파라미터의 총 수
        num_parameters = len(self.encoder.parameter_options)

        # 적합도 함수 정의
        def fitness_wrapper(encoded_params):
            return self.backtest_simulator.evaluation(encoded_params)

        # 유전 알고리즘 실행
        result = GA(num_agents=50, max_iter=100, train_data=np.zeros((1, num_parameters)),
                    train_label=np.zeros((1,)), obj_function=fitness_wrapper,
                    save_conv_graph=False)

        # 최적의 파라미터 조합 찾기
        optimal_encoded_params = result.best_agent
        optimal_params = self.encoder.decode(optimal_encoded_params)
        optimal_fitness = result.best_fitness

        return optimal_params, optimal_fitness