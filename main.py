from denoisingEncoder import logger
from denoisingEncoder.pipeline.stage_01_data_ingestion import DataIngestionPipeline


try:
    logger.info('>>>>>>>>>> Data Ingestion Stage Started <<<<<<<<<<')
    stage_01_obj = DataIngestionPipeline()
    stage_01_obj.main()
    logger.info('>>>>>>>>>> Data Ingestion Stage Completed <<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e
