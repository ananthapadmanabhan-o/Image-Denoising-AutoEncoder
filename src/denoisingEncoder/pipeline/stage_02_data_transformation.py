from denoisingEncoder.config.configuration import ConfigurationManager
from denoisingEncoder.components.data_transformation import DataTransformation
from denoisingEncoder import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform_data()


if __name__ == '__main__':

    try:
        logger.info('>>>>>>>>>> Data Transformation Stage Started <<<<<<<<<<')
        stage_02_obj = DataTransformationPipeline()
        stage_02_obj.main()
        logger.info('>>>>>>>>>> Data Transformation Stage Completed <<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e
    