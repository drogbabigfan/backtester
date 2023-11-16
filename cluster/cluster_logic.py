import pandas as pd
from abc import ABCMeta, abstractmethod # abstract base class

class ClusterLogic(metaclass=ABCMeta):
    
    @abstractmethod
    def get_raw_data(self, file_name: str):
        pass
    
    @abstractmethod
    def get_cluster_data(self, dataframe: pd.DataFrame):
        pass
  
    