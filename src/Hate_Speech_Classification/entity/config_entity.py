from dataclasses import dataclass
from Hate_Speech_Classification.constants import *
from Hate_Speech_Classification.logger import logging
import os

# @dataclass(frozen=True)
class DataIngestionConfig:
    def __init__(self):
        self.BUCKET_NAME :str = BUCKET_NAME
        self.BUCKET_FOLDER_NAME :str = BUCKET_FOLDER_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_INGESTION_ARTIFACTS_DIR)
        self.RAW_DATA_FILE_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR,DATA_INGESTION_IMBALANCE_DATA_DIR)
        self.IMBALANCED_DATA_FILE_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR,DATA_INGESTION_RAW_DATA_DIR)
        # self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        # self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR,self.ZIP_FILE_NAME)
        