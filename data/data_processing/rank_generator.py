from data.data_collector.data_handler import DataHandler
import pandas as pd
import os
from multiprocessing import Pool, cpu_count


class RankGenerator:
    def __init__(self):
        self.data_handler = DataHandler()
        self.csv_path = self.data_handler.csv_path

    def process_file(self, file_name):
        if 'price' in file_name:
            return

        print(file_name, "처리 시작")
        raw_data = self.data_handler.get_raw_data(file_name)
        rank = self.data_handler.calculate_rank(raw_data)
        rank.to_csv(os.path.join(self.csv_path, "rank", f"{file_name}.csv"))
        print(file_name, "처리 완료")

    def run(self):
        start_time = pd.Timestamp.now()
        raw_data_path = os.path.join(self.csv_path, "raw_data")
        file_list = self.data_handler.read_file_list(raw_data_path)

        # 멀티프로세싱을 사용하여 병렬 처리
        with Pool(cpu_count()) as pool:
            pool.map(self.process_file, file_list)

        end_time = pd.Timestamp.now()
        total_time = end_time - start_time
        print(f"total time: {total_time.total_seconds() / 60} min")


if __name__ == '__main__':
    rank_generator = RankGenerator()
    rank_generator.run()
