import concurrent.futures
import itertools
import os

import pandas as pd
from tqdm import tqdm

import data.data_processing.filter_calculator as filter_calculator
from backtest.parameter.momentum_parameters import MomentumParameters
from backtest.parameter.parameter_object import ParameterObject
from data.data_processing.data_handler import DataHandler


class BacktestDataBuilder:
    def __init__(self, parameter_object: ParameterObject, data_handler: DataHandler):
        self.filter_calculator = filter_calculator.FilterCalculator()
        self.parameter_dict = parameter_object.get_parameter_dict()
        self.data_handler = data_handler

    def generate_market_cap_filter(self, raw_data: pd.DataFrame):
        market_cap_filter_dict = self.generate_combinations(self.parameter_dict['market_cap_windows'],
                                                            self.parameter_dict['market_cap_select_criteria'],
                                                            self.parameter_dict['market_cap_select_counts'])

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_market_cap_filter, key, values, raw_data): key
                       for key, values in market_cap_filter_dict.items()}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                key = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{key} generated an exception: {e}")
                    print(f"{key} is skipped.")
                else:
                    print(f"{key} is processed.")

    def process_market_cap_filter(self, key, values, raw_data):
        period, select_criteria, select_count = values
        market_cap_filter = self.filter_calculator.market_cap_filter
        result = market_cap_filter.get_market_cap_filter(raw_data=raw_data, period=period,
                                                         threshold=select_count, criteria=select_criteria)
        if not result.empty:
            self.save_file(result, "market_cap_filter", key)

    def generate_transaction_amount_filter(self, raw_data: pd.DataFrame):
        transaction_filter_dict = self.generate_combinations(self.parameter_dict['transaction_amount_windows'],
                                                             self.parameter_dict['transaction_amount_select_counts'])

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_transaction_amount_filter, key, values, raw_data): key
                       for key, values in transaction_filter_dict.items()}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                key = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{key} generated an exception: {e}")
                    print(f"{key} is skipped.")
                else:
                    print(f"{key} is processed.")

    def process_transaction_amount_filter(self, key, values, raw_data):
        period, select_count = values

        if period == 0 or select_count == 0:
            print(f"{key} is skipped.")
            return

        transaction_filter = self.filter_calculator.transaction_filter
        result = transaction_filter.transaction_amount_filter(raw_data=raw_data, period=period,
                                                              threshold=select_count)
        if not result.empty:
            self.save_file(result, "transaction_amount_filter", key)

    def generate_turn_over_filter(self, raw_data: pd.DataFrame):
        turn_over_filter_dict = self.generate_combinations(self.parameter_dict['turn_over_windows'],
                                                           self.parameter_dict['turn_over_select_counts'])

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_turn_over_filter, key, values, raw_data): key
                       for key, values in turn_over_filter_dict.items()}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                key = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{key} generated an exception: {e}")
                    print(f"{key} is skipped.")
                else:
                    print(f"{key} is processed.")

    def process_turn_over_filter(self, key, values, raw_data):
        period, select_count = values

        if period == 0 or select_count == 0:
            print(f"{key} is skipped.")
            return

        turn_over_filter = self.filter_calculator.transaction_filter
        result = turn_over_filter.turn_over_filter(raw_data=raw_data, period=period,
                                                   threshold=select_count)
        if not result.empty:
            self.save_file(result, "turn_over_filter", key)

    def generate_volume_filter(self, raw_data: pd.DataFrame):
        volume_filter_dict = self.generate_combinations(self.parameter_dict['volume_windows'],
                                                        self.parameter_dict['volume_select_counts'])

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_volume_filter, key, values, raw_data): key
                       for key, values in volume_filter_dict.items()}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                key = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{key} generated an exception: {e}")
                    print(f"{key} is skipped.")
                else:
                    print(f"{key} is processed.")

    def process_volume_filter(self, key, values, raw_data):
        period, select_count = values

        if period == 0 or select_count == 0:
            print(f"{key} is skipped.")
            return

        volume_filter = self.filter_calculator.transaction_filter
        result = volume_filter.volume_filter(raw_data=raw_data, period=period,
                                             threshold=select_count)

        if not result.empty:
            self.save_file(result, "volume_filter", key)

    def generate_absolute_return_filter(self, raw_data: pd.DataFrame):
        absolute_return_filter_dict = self.generate_combinations(self.parameter_dict['absolute_return_windows'],
                                                                 self.parameter_dict['absolute_return_select_criteria'])

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_absolute_return_filter, key, values, raw_data): key
                       for key, values in absolute_return_filter_dict.items()}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                key = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{key} generated an exception: {e}")
                    print(f"{key} is skipped.")
                else:
                    print(f"{key} is processed.")

    def process_absolute_return_filter(self, key, values, raw_data):
        period, select_criteria = values
        result = pd.DataFrame()

        if period == 0:
            print(f"{key} is skipped.")
            return

        absolute_return_filter = self.filter_calculator.momentum_filter

        if select_criteria == "positive":
            result = absolute_return_filter.get_calculate_return_plus(raw_data=raw_data, window=period)
        elif select_criteria == "negative":
            result = absolute_return_filter.get_calculate_return_minus(raw_data=raw_data, window=period)
        else:
            print("Select Criteria 값이 이상하므로 확인 필요 : ", select_criteria)

        if not result.empty:
            self.save_file(result, "absolute_return_filter", key)

    def generate_period_return_data(self, raw_data: pd.DataFrame):
        momentum_windows = self.parameter_dict['momentum_windows']

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_period_return_data, window, raw_data): window
                       for window in momentum_windows}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                window = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{window} generated an exception: {e}")
                    print(f"{window} is skipped.")
                else:
                    print(f"{window} is processed.")

    def process_period_return_data(self, window, raw_data):
        result = pd.DataFrame()

        if window == 0:
            print(f"{window} is skipped.")
            return

        absolute_return_filter = self.filter_calculator.momentum_filter
        result = absolute_return_filter.calculate_period_return(raw_data=raw_data, window=window)

        if not result.empty:
            self.save_file(result, "period_return_data", window)

    def generate_momentum_rank_data(self, raw_data: pd.DataFrame):
        momentum_windows = self.parameter_dict['momentum_windows']

        # 병렬 처리를 위한 ThreadPoolExecutor 사용
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # futures 리스트 생성
            futures = {executor.submit(self.process_momentum_rank_data, window, raw_data): window
                       for window in momentum_windows}

            # tqdm을 사용하여 progress bar 추가
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing Filters"):
                window = futures[future]
                try:
                    result = future.result()
                except Exception as e:
                    print(f"{window} generated an exception: {e}")
                    print(f"{window} is skipped.")
                else:
                    print(f"{window} is processed.")

    def process_momentum_rank_data(self, window, raw_data):
        result = pd.DataFrame()

        if window == 0:
            print(f"{window} is skipped.")
            return

        absolute_return_filter = self.filter_calculator.momentum_filter
        result = absolute_return_filter.calculate_period_return(raw_data=raw_data, window=window)
        result = absolute_return_filter.util.calculate_rank(result)

        if not result.empty:
            self.save_file(result, "momentum_rank_data", window)

    def generate_ma_breakout_filter(self, raw_data: pd.DataFrame):
        ma_list = [5, 10, 20, 60, 120, 250]

        for ma in ma_list:
            upper_break = self.filter_calculator.ta_filter.get_ma_upper_breakout(raw_data=raw_data, window=ma)

            if not upper_break.empty:
                self.save_file(upper_break, f"technical_indicator_filter/ma{ma}", f"1")
                print(f"ma{ma} upper break is processed.")

            lower_break = self.filter_calculator.ta_filter.get_ma_lower_breakout(raw_data=raw_data, window=ma)

            if not lower_break.empty:
                self.save_file(lower_break, f"technical_indicator_filter/ma{ma}", f"2")
                print(f"ma{ma} lower break is processed.")

    def generate_bollinger_band_breakout_filter(self, raw_data: pd.DataFrame):
        upper_break_parm = self.parameter_dict['bband_upper_break']
        lower_break_parm = self.parameter_dict['bband_lower_break']

        ## parm의 key와 value를 분리해서 key = 0이면 pass
        for key, value in upper_break_parm.items():
            if key == 0:
                continue

            # value는 multiple, 파일명은 key 값으로 저장
            upper_break = self.filter_calculator.ta_filter.get_bollinger_band_upper_breakout(raw_data=raw_data,
                                                                                             window=20, multiple=value)

            if not upper_break.empty:
                self.save_file(upper_break, f"technical_indicator_filter/bband_upper_break", f"{key}")
                print(f"bband upper break {key} is processed.")

        for key, value in lower_break_parm.items():
            if key == 0:
                continue

            # value는 multiple, 파일명은 key 값으로 저장
            lower_break = self.filter_calculator.ta_filter.get_bollinger_band_lower_breakout(raw_data=raw_data,
                                                                                             window=20, multiple=value)

            if not lower_break.empty:
                self.save_file(lower_break, f"technical_indicator_filter/bband_lower_break", f"{key}")
                print(f"bband lower break {key} is processed.")

    def generate_bband_width_filter(self, raw_data: pd.DataFrame):
        bband_width_high_parm = self.parameter_dict['bband_width_high']
        bband_width_low_parm = self.parameter_dict['bband_width_low']

        for key, value in bband_width_high_parm.items():
            if key == 0:
                continue

            # value는 multiple, 파일명은 key 값으로 저장
            bband_width_high = self.filter_calculator.ta_filter.is_bollinger_band_width_high(raw_data=raw_data,
                                                                                             window=20, pct=value,
                                                                                             multiple=2)

            if not bband_width_high.empty:
                self.save_file(bband_width_high, f"technical_indicator_filter/bband_width_high", f"{key}")
                print(f"bband width high {key} is processed.")

        for key, value in bband_width_low_parm.items():
            if key == 0:
                continue

            # value는 multiple, 파일명은 key 값으로 저장
            bband_width_low = self.filter_calculator.ta_filter.is_bollinger_band_width_low(raw_data=raw_data,
                                                                                           window=20, pct=value,
                                                                                           multiple=2)

            if not bband_width_low.empty:
                self.save_file(bband_width_low, f"technical_indicator_filter/bband_width_low", f"{key}")
                print(f"bband width low {key} is processed.")

    def generate_bband_pctb_filter(self, raw_data: pd.DataFrame):
        bband_pctb_high_parm = self.parameter_dict['bband_pctb_high']
        bband_pctb_low_parm = self.parameter_dict['bband_pctb_low']

        for key, value in bband_pctb_high_parm.items():
            if key == 0:
                continue

            # value는 multiple, 파일명은 key 값으로 저장
            bband_pctb_high = self.filter_calculator.ta_filter.is_bollinger_band_pctb_high(raw_data=raw_data,
                                                                                           window=20, multiple=2,
                                                                                           pct=value)

            if not bband_pctb_high.empty:
                self.save_file(bband_pctb_high, f"technical_indicator_filter/bband_pctb_high", f"{key}")
                print(f"bband pctb high {key} is processed.")

        for key, value in bband_pctb_low_parm.items():
            if key == 0:
                continue

            # value는 multiple, 파일명은 key 값으로 저장
            bband_pctb_low = self.filter_calculator.ta_filter.is_bollinger_band_pctb_low(raw_data=raw_data,
                                                                                         window=20, multiple=2,
                                                                                         pct=value)

            if not bband_pctb_low.empty:
                self.save_file(bband_pctb_low, f"technical_indicator_filter/bband_pctb_low", f"{key}")
                print(f"bband pctb low {key} is processed.")

    def generate_ma_positive_arranged_filter(self, raw_data: pd.DataFrame):
        ma_positive_arranged = self.filter_calculator.ta_filter.is_ma_positive_arranged(raw_data=raw_data)

        if not ma_positive_arranged.empty:
            self.save_file(ma_positive_arranged, f"technical_indicator_filter/ma_positive_arranged", f"1")
            print(f"ma positive arranged is processed.")

    def generate_ma_negative_arranged_filter(self, raw_data: pd.DataFrame):
        ma_negative_arranged = self.filter_calculator.ta_filter.is_ma_negative_arranged(raw_data=raw_data)

        if not ma_negative_arranged.empty:
            self.save_file(ma_negative_arranged, f"technical_indicator_filter/ma_negative_arranged", f"1")
            print(f"ma negative arranged is processed.")

    def run_data_builder(self):
        volume_df = self.data_handler.get_csv_raw_data("all_volume.csv")
        transaction_value_df = self.data_handler.get_csv_raw_data("all_transaction_value.csv")
        marcap_df = self.data_handler.get_csv_raw_data("all_marcap.csv")
        turn_over_df = transaction_value_df / marcap_df

        print("Generating Filters...")
        print("Generating Market Cap Filter...")
        self.generate_market_cap_filter(marcap_df)
        print("Generating Transaction Amount Filter...")
        self.generate_transaction_amount_filter(transaction_value_df)
        print("Generating Turn Over Filter...")
        self.generate_turn_over_filter(turn_over_df)
        print("Generating Volume Filter...")
        self.generate_volume_filter(volume_df)
        print("Generating Absolute Return Filter...")
        self.generate_absolute_return_filter(marcap_df)
        print("Generating Period Return Data...")
        self.generate_period_return_data(marcap_df)
        print("Generating Momentum Rank Data...")
        self.generate_momentum_rank_data(marcap_df)

        # ta filter
        print("Generating MA Breakout Filter...")
        self.generate_ma_breakout_filter(marcap_df)
        print("Generating Bollinger Band Breakout Filter...")
        self.generate_bollinger_band_breakout_filter(marcap_df)
        print("Generating Bollinger Band Width Filter...")
        self.generate_bband_width_filter(marcap_df)
        print("Generating Bollinger Band Pctb Filter...")
        self.generate_bband_pctb_filter(marcap_df)
        print("Generating MA Positive Arranged Filter...")
        self.generate_ma_positive_arranged_filter(marcap_df)
        print("Generating MA Negative Arranged Filter...")
        self.generate_ma_negative_arranged_filter(marcap_df)

    @staticmethod
    def generate_combinations(*dicts):
        return {"_".join(map(str, combo)): [d[k] for d, k in zip(dicts, combo)]
                for combo in itertools.product(*[d.keys() for d in dicts])}

    def save_file(self, df: pd.DataFrame, folder_name: str, file_name: str):
        csv_file_path = os.path.join(self.data_handler.processed_data_csv_path, folder_name, f"{file_name}.csv")
        parquet_file_path = os.path.join(self.data_handler.processed_data_parquet_path, folder_name,
                                         f"{file_name}.parquet")

        df.to_csv(csv_file_path, index=False)
        df.to_parquet(parquet_file_path, index=False)


if __name__ == "__main__":
    data_handler = DataHandler()
    parameter_object = MomentumParameters()
    backtest_data_builder = BacktestDataBuilder(parameter_object, data_handler)
    backtest_data_builder.run_data_builder()
