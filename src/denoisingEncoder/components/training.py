from denoisingEncoder.entity.config_entity import TrainingConfig
from denoisingEncoder.utils.common import load_pkl,save_pkl
from pathlib import Path
import tensorflow as tf
from denoisingEncoder import logger

class Training:
    def __init__(self,config:TrainingConfig):
        self.config = config

    
    def begin_training(self):
        x_train = load_pkl(Path(self.config.local_input_feature_file))
        y_train = load_pkl(Path(self.config.local_output_feature_file))
        model = load_pkl(Path(self.config.base_model_path))
        device = 'GPU' if len(tf.config.list_physical_devices('GPU')) > 0 else 'CPU'
        logger.info(f'{device} initiated for training')
        if device == 'GPU':
            tf.config.experimental.set_memory_growth(tf.device('GPU'),True)
            logger.info(f'Memory growth enabled for {device}')
        
        with tf.device(device):
            logger.info(f'Model Started Training using device {device}')
            model.fit(x_train,y_train,batch_size=self.config.params_batch_size,epochs=self.config.params_epochs)
            logger.info('Model Trained Successfully')
        save_pkl(model,Path(self.config.trained_model_path))