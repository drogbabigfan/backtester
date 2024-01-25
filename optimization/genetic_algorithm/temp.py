
# class GeneticAlgorithmOptimizer:
#     def __init__(self, parameter_encoder: ParameterEncoderDecoder, backtest_simulator: BacktesterForOptimization):
#         self.parameter_encoder = parameter_encoder
#         self.backtest_simulator = backtest_simulator
#
#     def set_initial_population(self, num_agents: int, num_parameters: int, parameter_dict: dict):
#         initial_population = np.zeros((num_agents, num_parameters))
#
#         for i in range(num_parameters):
#             # 현재 파라미터에 대한 가능한 값 추출
#             param_item = list(parameter_dict.values())[i]
#             if i == 0 or i == 1:
#                 param_values = list(range(len(param_item)))
#                 initial_population[:, i] = np.random.choice(param_values, size=num_agents)
#                 continue
#             elif 2 <= i <= 5:
#                 param_values = list(param_item.keys())
#                 initial_population[:, i] = np.random.choice(param_values, size=num_agents)
#                 continue
#             elif i == 6:
#                 # market_cap_select_criteria - large
#                 initial_population[:, i] = 1
#                 continue
#             elif i == 7:
#                 # market_cap_select_counts
#                 param_values = list(param_item.keys())
#                 initial_population[:, i] = np.random.choice(param_values, size=num_agents)
#                 continue
#             elif 8 <= i <= 13:
#                 initial_population[:, i] = 0
#                 continue
#             elif i == 14:
#                 # absolute_return_windows
#                 param_values = [1, 2, 3, 4, 7, 8]
#                 initial_population[:, i] = np.random.choice(param_values, size=num_agents)
#                 continue
#             elif i == 15:
#                 # absolute_return_select_counts
#                 param_values = list(param_item.keys())
#                 initial_population[:, i] = np.random.choice(param_values, size=num_agents)
#                 continue
#             elif i >= 16:
#                 initial_population[:, i] = 0
#                 continue
#
#         return initial_population
#
#     def run(self, num_parameters: int, num_agents: int, max_iter: int, parameter_dict: dict):
#         # 적합도 함수 정의
#         def fitness_wrapper(encoded_params, *args):
#             return self.backtest_simulator.evaluation(encoded_params)
#
#         train_data = self.set_initial_population(num_agents=num_agents, num_parameters=num_parameters,
#                                                  parameter_dict=parameter_dict)
#
#         # 임시 train_label 생성
#         train_label = np.zeros(len(train_data))
#
#         # 유전 알고리즘 실행
#         result = GA(num_agents=num_agents, max_iter=max_iter, train_data=train_data,
#                     train_label=train_label, obj_function=fitness_wrapper,
#                     save_conv_graph=False)
#
#         # 최적의 파라미터 조합 찾기
#         optimal_encoded_params = result.best_agent
#         optimal_params = self.parameter_encoder.decode_to_value(optimal_encoded_params)
#         optimal_fitness = result.best_fitness
#
#         return optimal_params, optimal_fitness
