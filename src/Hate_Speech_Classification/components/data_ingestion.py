import os
import sys
from Hate_Speech_Classification.logger import logging
from Hate_Speech_Classification.exception import CustomException
from Hate_Speech_Classification.configuration.aws_syncer import AwsSync
from Hate_Speech_Classification.entity.config_entity import DataIngestionConfig
from Hate_Speech_Classification.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig)-> None:
        self.data_ingestion_config = data_ingestion_config
        self.aws_sync = AwsSync()

    def get_data_from_aws(self)-> None:
        try:
            logging.info("Entered the get_data_from_aws method od DataIngestion class")
            self.aws_sync.sync_folder_from_s3(
                folder=self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,
                bucket_name=self.data_ingestion_config.BUCKET_NAME,
                bucket_folder_name=self.data_ingestion_config.BUCKET_FOLDER_NAME
            )
            logging.info("Exited teh get_data_from_aws method of DataIngestion class")
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def initiate_data_ingestion(self)->DataIngestionArtifacts:
        try:
            logging.info("Entered initiate_data_ingestion method of DataIngestion class")
            self.get_data_from_aws()
            logging.info("Fetched data from AWS S3 bucket")
            return DataIngestionArtifacts(
                imbalance_data_file_path=self.data_ingestion_config.IMBALANCED_DATA_FILE_PATH,
                raw_data_file_path=self.data_ingestion_config.RAW_DATA_FILE_PATH
            )
        except Exception as e:
            raise CustomException(e,sys) from e