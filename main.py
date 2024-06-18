from denoisingEncoder import logger
from denoisingEncoder.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from denoisingEncoder.pipeline.stage_02_data_transformation import DataTransformationPipeline

try:
    logger.info('>>>>>>>>>> Data Ingestion Stage Started <<<<<<<<<<')
    stage_01_obj = DataIngestionPipeline()
    stage_01_obj.main()
    logger.info('>>>>>>>>>> Data Ingestion Stage Completed <<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e



try:
    logger.info('>>>>>>>>>> Data Transformation Stage Started <<<<<<<<<<')
    stage_02_obj = DataTransformationPipeline()
    stage_02_obj.main()
    logger.info('>>>>>>>>>> Data Transformation Stage Completed <<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e