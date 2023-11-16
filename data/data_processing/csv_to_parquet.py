import data.data_processing.data_handler as data_handler

class CsvToParquet:
    def __init__(self):
        self.data_handler = data_handler.DataHandler()
        self.csv_path = self.data_handler.csv_path
        self.parquet_path = self.data_handler.parquet_path