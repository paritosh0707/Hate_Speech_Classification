from Hate_Speech_Classification.logger import logging 
from Hate_Speech_Classification.exception import CustomException 
import os
import sys
    
class S3Openration:

    def __init__(self) -> None:
        pass
    
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        logging.info("Entered sync_folder_to_s3 method of S3Operation class")
        try:
            command: str = (
                f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/"
            )
            logging.info("executing s3 data sync command")
            os.system(command)
            logging.info("Exited sync_folder_to_s3 method of S3Operation class")
        except Exception as e:
            raise CustomException(e,sys)
        
    def sync_folder_from_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        logging.info("Entered sync_folder_from_s3 method of S3Operation class")
        try:
            command: str = (
                f"aws s3 sync s3://{bucket_name}/{bucket_folder_name} {folder}"
            )
            logging.info("executing s3 data sync command")
            os.system(command)
            logging.info("Exited sync_folder_from_s3 method of S3Operation class")
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    sync_operations = S3Openration()
    sync_operations.sync_folder_from_s3(
        bucket_name="hate-speech-classifier",
        bucket_folder_name="dataset",
        folder="data"
    )