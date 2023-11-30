class Individual:
    def __init__(self, parameters):
        self.parameter = parameters
        self.fitness = 0.0

    def evlauation_fitness(self):
        # 개체 적합도 평가
        backtest_result = run_backtest(self.parameter)
        cagr, mdd = calculate_cagr_mdd(backtest_result)
        self.fintess = cagr/mdd