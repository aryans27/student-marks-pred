import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass       # used to create class variables

@dataclass
class DataIngestionCofig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionCofig()      # the 3 path var will get saved in this var when it is created

    def initiate_data_ingestion(self):
        logging.info("Initiating Data Ingestion")

        try:
            df=pd.read_csv('notebooks/data/student_data.csv')
            logging.info('Read dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)
            logging.info("Train test split initiated")
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header=True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()