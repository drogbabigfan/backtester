import threading

import numpy as np
from joblib._multiprocessing_helpers import mp



class GeneticAlgorithmOptimizer:
    def __init__(self, num_agents, num_parameters, parameter_dict, num_generations, num_parents_mating,
                 backtest_simulator):
        self.num_agents = num_agents
        self.num_parameters = num_parameters
        self.parameter_dict = parameter_dict
        self.num_generations = num_generations
        self.num_parents_mating = num_parents_mating
        self.backtest_simulator = backtest_simulator
        self.population = self._create_initial_population(num_agents, num_parameters, parameter_dict)

    def _create_initial_population(self, num_agents: int, num_parameters: int, parameter_dict: dict):
        initial_population = np.zeros((num_agents, num_parameters))

        for i in range(num_parameters):
            # 현재 파라미터에 대한 가능한 값 추출
            param_item = list(parameter_dict.values())[i]
            if i == 0 or i == 1:
                param_values = list(range(len(param_item)))
                initial_population[:, i] = np.random.choice(param_values, size=num_agents)
                continue
            elif 2 <= i <= 5:
                param_values = list(param_item.keys())
                initial_population[:, i] = np.random.choice(param_values, size=num_agents)
                continue
            elif i == 6:
                # market_cap_select_criteria - large
                initial_population[:, i] = 1
                continue
            elif i == 7:
                # market_cap_select_counts
                param_values = list(param_item.keys())
                initial_population[:, i] = np.random.choice(param_values, size=num_agents)
                continue
            elif 8 <= i <= 13:
                # volume_windows, volume_select_counts, transaction_amount_windows, transaction_amount_select_counts,
                # turn_over_windows, turn_over_select_counts
                param_values = list(param_item.keys())
                # Ensure that either both are 0 or both are non-zero
                for agent in range(num_agents):
                    value = np.random.choice(param_values)
                    initial_population[agent, i] = value
                    initial_population[agent, i + 1] = value if value != 0 else np.random.choice(param_values[1:])
                i += 1  # Skip the next parameter as it's already handled
                continue
            elif i == 14:
                # absolute_return_windows
                param_values = [1, 2, 3, 4, 7, 8]
                initial_population[:, i] = np.random.choice(param_values, size=num_agents)
                continue
            elif i == 15:
                # absolute_return_select_criteria
                param_values = list(param_item.keys())
                initial_population[:, i] = np.random.choice(param_values, size=num_agents)
                continue

            # elif i >= 16:
            #     initial_population[:, i] = 0
            #     continue

        return initial_population

    def fitness_wrapper(self, encoded_params):
        return self.backtest_simulator.evaluation(encoded_params)

    # def _evaluate_population(self):
    #     """인구 평가"""
    #     fitness_scores = [self.fitness_wrapper(individual) for individual in self.population]
    #     return np.array(fitness_scores)

    def _evaluate_population_thread(self, individual, fitness_scores, idx):
        fitness_score = self.fitness_wrapper(individual)
        fitness_scores[idx] = fitness_score

    def _evaluate_population(self):
        threads = []
        fitness_scores = [None] * len(self.population)
        for idx, individual in enumerate(self.population):
            thread = threading.Thread(target=self._evaluate_population_thread, args=(individual, fitness_scores, idx))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return np.array(fitness_scores)

    def _select_parents(self, fitness_scores):
        """부모 선택"""
        parents = np.empty((self.num_parents_mating, self.population.shape[1]))
        for i in range(self.num_parents_mating):
            max_fitness_idx = np.argmax(fitness_scores)
            parents[i, :] = self.population[max_fitness_idx, :]
            fitness_scores[max_fitness_idx] = -99999999
        return parents

    def _crossover(self, parents):
        """교차"""
        offspring_size = (self.num_agents - parents.shape[0], self.population.shape[1])
        offspring = np.empty(offspring_size)

        for k in range(offspring_size[0]):
            # 무작위 교차점 선택
            crossover_point = np.random.randint(1, self.num_parameters - 1)

            # 부모 선택
            parent1_idx = k % parents.shape[0]
            parent2_idx = (k + 1) % parents.shape[0]

            # 교차하여 자손 생성
            offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
            offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

        return offspring

    def _mutate(self, offspring):
        """돌연변이"""
        params = list(self.parameter_dict.values())
        for idx in range(offspring.shape[0]):
            mutation_index = np.random.randint(0, self.num_parameters)
            if mutation_index == 0:
                param_values = params[0]
                param_values = list(range(len(param_values)))
                offspring[idx, mutation_index] = np.random.choice(param_values)
            elif mutation_index == 1:
                param_values = params[1]
                param_values = list(range(len(param_values)))
                offspring[idx, mutation_index] = np.random.choice(param_values)
            elif 2 <= mutation_index:
                params_values = params[mutation_index]
                params_keys = list(params_values.keys())
                offspring[idx, mutation_index] = np.random.choice(params_keys)
        return offspring

    def run(self):
        """유전 알고리즘 실행"""
        for generation in range(self.num_generations):
            print("Generation : ", generation)
            fitness_scores = self._evaluate_population()
            parents = self._select_parents(fitness_scores)
            offspring = self._crossover(parents)
            offspring_mutation = self._mutate(offspring)
            self.population[0:parents.shape[0], :] = parents
            self.population[parents.shape[0]:, :] = offspring_mutation
        fitness_scores = self._evaluate_population()
        best_match_idx = np.where(fitness_scores == np.max(fitness_scores))
        best_match_idx = best_match_idx[0][0]
        best_solution = self.population[best_match_idx, :]
        best_solution_fitness = fitness_scores[best_match_idx]
        return best_solution, best_solution_fitness