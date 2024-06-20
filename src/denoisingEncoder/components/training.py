from denoisingEncoder.entity.config_entity import TrainingConfig
from denoisingEncoder.utils.common import load_pkl,save_pkl, create_directories
from pathlib import Path
import tensorflow as tf
from denoisingEncoder import logger
import keras


class Training:
    def __init__(self,config:TrainingConfig):
        self.config = config

    
    def begin_training(self):
        
        keras.backend.clear_session()
        logger.info('keras backend session cleared')
        x_train = load_pkl(Path(self.config.local_input_feature_file))
        y_train = load_pkl(Path(self.config.local_output_feature_file))
        model = load_pkl(Path(self.config.base_model_path))
        device = 'GPU' if len(tf.config.list_physical_devices('GPU')) > 0 else 'CPU'
        logger.info(f'{device} enabled for training')
        
        with tf.device(device):
            logger.info(f'Model Training started using device {device}')
            model.fit(x_train,y_train,batch_size=self.config.params_batch_size,epochs=self.config.params_epochs)
            logger.info('Model Trained Successfully')
        save_pkl(model,Path(self.config.trained_model_path))
        create_directories(['assets/model'])
        save_pkl(model,Path('assets/model/model.pkl'))
        