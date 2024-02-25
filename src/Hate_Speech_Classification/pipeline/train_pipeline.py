import sys
import os
from Hate_Speech_Classification.components.data_ingestion import DataIngestion
from Hate_Speech_Classification.components.data_transforamation import DataTransformation
from Hate_Speech_Classification.components.model_trainer import ModelTrainer
from Hate_Speech_Classification.logger import logging
from Hate_Speech_Classification.exception import CustomException
from Hate_Speech_Classification.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
from Hate_Speech_Classification.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts, ModelTrainerArtifacts


class TrainingPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()

    def start_data_ingestion(self)-> DataIngestionArtifacts:
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
        
    def start_data_transformation(self, data_ingestion_artifacts = DataIngestionArtifacts) -> DataTransformationArtifacts:
        logging.info("Entered the start_data_transformation method of TrainPipeline class")
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifacts = data_ingestion_artifacts,
                data_transformation_config=self.data_transformation_config
            )

            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            
            logging.info("Exited the start_data_transformation method of TrainPipeline class")
            return data_transformation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        

    def start_model_trainer(self, data_transformation_artifacts: DataTransformationArtifacts) -> ModelTrainerArtifacts:
        logging.info(
            "Entered the start_model_trainer method of TrainPipeline class"
        )
        try:
            model_trainer = ModelTrainer(data_transformation_artifacts=data_transformation_artifacts,
                                        model_trainer_config=self.model_trainer_config
                                        )
            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            logging.info("Exited the start_model_trainer method of TrainPipeline class")
            return model_trainer_artifacts

        except Exception as e:
            raise CustomException(e, sys) 
        

    def run_pipeline(self)->None:
        logging.info("Entering run_pipeline method of TrainingPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )
            model_trainer_artifacts = self.start_model_trainer(
                data_transformation_artifacts=data_transformation_artifacts
            )
        except Exception as e:
            raise CustomException(e,sys) from e
        