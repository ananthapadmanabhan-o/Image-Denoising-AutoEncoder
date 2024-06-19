from denoisingEncoder.config.configuration import ConfigurationManager
from denoisingEncoder.components.base_model import BaseModel
from denoisingEncoder import logger



class BaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.build_model()



if __name__=='__main__':
    try:
        logger.info('>>>>>>>>>> Base Model Stage Started <<<<<<<<<<')
        stage_03_obj = BaseModelPipeline()
        stage_03_obj.main()
        logger.info('>>>>>>>>>> Base Model Stage completed <<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e