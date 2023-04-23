import os
import sys
import glob

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the initiate data ingestion')
        try:
            df = pd.read_csv('data/StudentsPerformance.csv')
            # csv_files = glob.glob(os.path.join("data", "*.csv"))
            # df = pd.DataFrame()

            # for f in csv_files:
            #     temp_df = pd.read_csv(f)
            #     main_df = pd.concat([temp_df, df])

            # logging.info('Read the dataset as df')
            # os.makedirs(os.path.dirname(
            #     self.ingestion_config.test_data_path), exist_ok=True)
            # df.to_csv(self.ingestion_config.raw_data_path,
            #           index=False, header=True)

            # logging.info(
            #     'combined all csvs into one and moved to raw data folder')
            # for f in csv_files:
            #     os.remove(f)

            logging.info('Initiating Train Test Split')
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)
            logging.info('Train test split completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)  # type: ignore


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data)
    model_trainer = ModelTrainer()
    score = model_trainer.initiate_model_trainer(train_arr, test_arr)
    print(score)
