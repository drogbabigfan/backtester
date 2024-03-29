import bt
import pandas as pd

from backtest.bakctester.backtester_for_optimization import BacktesterForOptimization
from backtest.bakctester.momentum_backtest.get_calculated_df import GetCalculatedDf
from backtest.bakctester.momentum_backtest.parameter_dispenser import ParameterDispenser
from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_encoder import ParameterEncoderDecoder
from data.data_reader.data_reader import BackTestDataReader
from db.backtest_result.momentum_strategy.backest_result_service import BacktestResultService


class MomentumStrategyBacktester(BacktesterForOptimization):
    def __init__(self, momentum_parameter: MomentumParameters, parameter_encoder: ParameterEncoderDecoder):
        self.momentum_parameter = momentum_parameter
        self.parameter_encoder = parameter_encoder
        self.get_calculated_df = GetCalculatedDf(self.momentum_parameter)
        self.parameter_dispenser = ParameterDispenser(momentum_parameters=self.momentum_parameter,
                                                      get_calculated_df=self.get_calculated_df)
        self.backtest_result_service = BacktestResultService()

    def run_backtest(self, parameter_list: list):
        print("run_backtest : ", parameter_list)
        if self.is_not_validate_parameter(parameter_list):
            return 0

        parameter_index_dict = self.parameter_encoder.decode_to_index(parameter_list)

        price_data = BackTestDataReader().get_market_cap_parquet()
        strategy = self.parameter_dispenser.get_momentum_strategy(parameter_dict=parameter_index_dict, price=price_data)

        if strategy is None:
            return 0

        backtest = bt.Backtest(strategy, price_data)

        result = bt.run(backtest)

        return result

    def evaluation(self, parameter_list: list):
        if self.is_not_validate_parameter(parameter_list):
            print("is_not_validate_parameter : ", parameter_list)
            return 0

        backtest_result = self.run_backtest(parameter_list)
        print("backtest 완료 : ", parameter_list)

        if backtest_result == 0:
            print("backtest_result == 0 : ", parameter_list)
            return 0

        strategy_name = backtest_result.stats.columns[0]
        stats = backtest_result.stats.T

        # 매매횟수
        try:
            trades = backtest_result.get_transactions(strategy_name)
            # 연간 10회 이하 매매는 제외
            if len(trades) < 170:
                print("len(trades) < 170 : ", parameter_list)
                return 0
        except IndexError:
            print("매매횟수 0회 : ", parameter_list)
            return 0

        self.save_backtest_result(strategy_name=strategy_name, backtest_result=backtest_result)

        cagr = stats['cagr'].values[0]
        mdd = stats['max_drawdown'].values[0]
        score = cagr - 2 * mdd

        print('cagr : ', cagr)
        print('mdd : ', mdd)
        print('score : ', score)
        return score

    def save_backtest_result(self, strategy_name: str, backtest_result: pd.DataFrame):
        self.backtest_result_service.upload_backtest_result(strategy_name=strategy_name,
                                                            backtest_result=backtest_result)

    # parameter 검증
    def is_not_validate_parameter(self, parameter_list: list):
        parameter_dict = self.parameter_encoder.decode_to_value(parameter_list)
        momentum_parameter_dict = self.momentum_parameter.get_parameter_dict()

        for key, value in parameter_dict.items():
            momentum_paramter = momentum_parameter_dict[key]

            if isinstance(momentum_paramter, dict):
                if value not in momentum_paramter.values():
                    print('parameter error : ', momentum_paramter, key, value)
                    return True
            else:
                if value not in momentum_paramter:
                    print('parameter error : ', momentum_paramter, key, value)
                    return True
