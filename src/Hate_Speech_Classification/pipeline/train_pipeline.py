import sys
import os
from Hate_Speech_Classification.components.data_ingestion import DataIngestion
from Hate_Speech_Classification.logger import logging
from Hate_Speech_Classification.exception import CustomException
from Hate_Speech_Classification.entity.config_entity import DataIngestionConfig
from Hate_Speech_Classification.entity.artifact_entity import DataIngestionArtifacts


class TrainingPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self)-> DataIngestionArtifacts:
        logging.info("Entered initiate_data_ingestion method of TrainingPipeline class")
        try:
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            logging.info("Getting data from AWS S3 bucket")
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Exited the intiate_data_ingestion method of TrainingPipeline class")
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def run_pipeline(self)->None:
        logging.info("Entering run_pipeline method of TrainingPipeline class")
        try:
            data_ingestion_artifacts = self.initiate_data_ingestion()
            print(data_ingestion_artifacts.imbalance_data_file_path)
            print(data_ingestion_artifacts.raw_data_file_path)
        except Exception as e:
            raise CustomException(e,sys) from e
        