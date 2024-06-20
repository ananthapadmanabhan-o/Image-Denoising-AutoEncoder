from denoisingEncoder.config.configuration import ConfigurationManager
from denoisingEncoder.components.training import Training
from denoisingEncoder import logger


class TrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.begin_training()


if __name__ == '__main__':

    try:        
        logger.info('>>>>>>>>>> Training Stage Started <<<<<<<<<<')
        stage_04_obj = TrainingPipeline()
        stage_04_obj.main()
        logger.info('>>>>>>>>>> Training Stage Completed <<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e

