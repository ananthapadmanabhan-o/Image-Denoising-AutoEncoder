from denoisingEncoder.config.configuration import ConfigurationManager
from denoisingEncoder.components.data_ingestion import DataIngestion
from denoisingEncoder import logger


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == '__main__':

    try:
        logger.info('>>>>>>>>>> Data Ingestion Stage Started <<<<<<<<<<')
        stage_01_obj = DataIngestionPipeline()
        stage_01_obj.main()
        logger.info('>>>>>>>>>> Data Ingestion Stage Completed <<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e
    