from denoisingEncoder import logger
from denoisingEncoder.entity.config_entity import DataTransformationConfig
from denoisingEncoder.utils.common import save_pkl
import numpy as np
from tqdm import tqdm
import os
from pathlib import Path
from skimage.transform import resize
from skimage.io import imread


def add_noise(img,sig=30):
    sigma = sig/255
    noise = np.random.normal(scale=sigma,size=img.shape)
    noisy_img = np.clip(img+noise,0,1).astype(np.float32)
    return noisy_img


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config


    def transform_data(self):
        logger.info('data transformation initialized')
        dir_path = self.config.local_data_source_path
        img_height = self.config.image_height
        img_width = self.config.image_width
        img_dataset = []
        noise_dataset = []
        for img_file in tqdm(os.listdir(os.path.join(dir_path))):
            img_file_path = os.path.join(dir_path,img_file)

            img = (imread(img_file_path)/255).astype(np.float32)
            img = resize(img,(img_height,img_width))
            noise_img = add_noise(img)
            img_dataset.append(img)
            noise_dataset.append(noise_img)
        

        img_dataset = np.array(img_dataset)
        noise_dataset = np.array(noise_dataset)
        logger.info('data transformed successfully')

        save_pkl(img_dataset,Path(self.config.local_output_feature_file))
        save_pkl(noise_dataset,Path(self.config.local_input_feature_file))



        