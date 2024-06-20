from keras.layers import Conv2D ,MaxPooling2D, Input, Conv2DTranspose, Dropout , concatenate
from keras.optimizers import Adam
from keras import Model
import tensorflow as tf
from denoisingEncoder.entity.config_entity import BaseModelConfig
from denoisingEncoder import logger
from pathlib import Path
from denoisingEncoder.utils.common import save_pkl




class BaseModel:
    def __init__(self,config:BaseModelConfig):
        self.config = config
    


    
    def build_model(self):

        logger.info('Model Building Initiated')

        tf.keras.backend.clear_session()
        input_layer = Input((self.config.image_width,self.config.image_height,self.config.image_channel))

        # encoder

        # 256_256_3
        c1 = Conv2D(32,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(input_layer)
        c1 = Dropout(0.2)(c1)
        c1 = Conv2D(32,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(c1)
        p1 = MaxPooling2D((2,2))(c1)
        # 128_128_32

        # 128_128_32
        c2 = Conv2D(64,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(p1)
        c2 = Dropout(0.2)(c2)
        c2 = Conv2D(64,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(c2)
        p2 = MaxPooling2D((2,2))(c2)
        # 64_64_64

        # 64_64_64
        c3 = Conv2D(128,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(p2)
        c3 = Dropout(0.2)(c3)
        c3 = Conv2D(128,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(c3)
        p3 = MaxPooling2D((2,2))(c3)
        # 32_32_128

        # 32_32_128
        c4 = Conv2D(256,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(p3)
        c4 = Dropout(0.2)(c4)
        c4 = Conv2D(256,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(c4)
        p4 = MaxPooling2D((2,2))(c4)
        # 16_16_256

        # bottleneck

        # 16_16_256
        c5 = Conv2D(256,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(p4)
        c5 = Dropout(0.2)(c4)
        c5 = Conv2D(256,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(c4)
        # 16_16_256

        # decoder

        # 16_16_256
        d1 = Conv2DTranspose(256,(3,3),strides=(2,2),padding='same')(c5)
        # 32_32_256

        # 32_32_256
        d1 = concatenate([d1,c3])
        # 32_32_256

        # 32_32_256
        d1 = Conv2D(128,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d1)
        d1 = Dropout(0.2)(d1)
        d1 = Conv2D(128,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d1)
        # 32_32_128

        # 32_32_128
        d2 = Conv2DTranspose(128,(3,3),strides=(2,2),padding='same')(d1)
        # 64_64_128

        # 64_64_128
        d2 = concatenate([d2,c2])
        d2 = Conv2D(64,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d2)
        d2 = Dropout(0.2)(d2)
        d2 = Conv2D(64,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d2)
        # 64_64_64

        # 64_64_64
        d3 = Conv2DTranspose(64,(3,3),strides=(2,2),padding='same')(d2)
        # 128_128_64

        # 128_128_64
        d3 = concatenate([d3,c1])
        d3 = Conv2D(32,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d3)
        d3 = Dropout(0.2)(d3)
        d3 = Conv2D(32,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d3)
        # 128_128_32

        # 128_128_32
        d4 = Conv2DTranspose(32,(3,3),strides=(2,2),padding='same')(d2)
        # 256_256_32

        # 256_256_32
        d4 = concatenate([d4,c1])
        d4 = Conv2D(16,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d4)
        d4 = Dropout(0.2)(d4)
        d4 = Conv2D(16,(3,3),activation='relu',kernel_initializer='he_normal',padding='same')(d4)
        # 256_256_16

        outputs = Conv2D(3,(3,3),activation='sigmoid',padding='same')(d4)

        # output 256_256_3

        model = Model(inputs = [input_layer],outputs = [outputs])
        model.compile(optimizer=Adam(learning_rate= self.config.learning_rate), loss='mse', metrics=['accuracy'])


        logger.info('Model Compiled Successfully')

        save_pkl(model,Path(self.config.base_model_path))
        logger.info('Untrained Model Saved Successfully')

