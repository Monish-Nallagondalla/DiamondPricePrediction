import os
import sys
from src.logger import logging
from src.exception import CustomException

import   pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

## initialise the data ingestion configuration 

@dataclass # directly creaing class variables 

class DataIngestionConfig:
    train_data_path:str = os.path.join('artificats','train.csv')
    test_data_path:str = os.path.join('artificats','test.csv')
    raw_data_path:str = os.path.join('artificats','raw.csv')

## Create the data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            df = pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.join(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path)
            logging.info('Raw data is created')

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)