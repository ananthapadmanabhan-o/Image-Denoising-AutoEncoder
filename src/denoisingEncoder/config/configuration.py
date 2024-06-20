from denoisingEncoder.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from denoisingEncoder.utils.common import read_yaml, create_directories
from denoisingEncoder.entity.config_entity import (DataIngestionConfig,
                                                   DataTransformationConfig,
                                                   BaseModelConfig,
                                                   TrainingConfig
                                                   )

import os



class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_path=PARAMS_FILE_PATH
                 ):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    


    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation
        params = self.params

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            local_data_source_path=config.local_data_source_path,
            local_input_feature_file=config.local_input_feature_file,
            local_output_feature_file=config.local_output_feature_file,
            image_height=params.IMAGE_HEIGHT,
            image_width=params.IMAGE_WIDTH,
            image_channel=params.IMAGE_CHANNEL
        )

        return data_transformation_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model
        params = self.params

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=config.root_dir,
            base_model_path= config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            image_height = params.IMAGE_HEIGHT,
            image_width = params.IMAGE_WIDTH,
            image_channel = params.IMAGE_CHANNEL,
            learning_rate= params.LEARNING_RATE
        )

        return base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        config = self.config.training
        params = self.params

        create_directories([config.root_dir])

        training_config = TrainingConfig(
            root_dir = config.root_dir,
            base_model_path= config.base_model_path,
            trained_model_path =config.trained_model_path,
            local_input_feature_file= config.local_input_feature_file,
            local_output_feature_file=config.local_output_feature_file,    
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE
        )

        return training_config