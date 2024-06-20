from denoisingEncoder.utils.common import load_pkl,read_yaml
from denoisingEncoder.constants import PARAMS_FILE_PATH
from pathlib import Path
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from denoisingEncoder import logger




class PredictionPipeline:
    def __init__(self,img_file):
        self.img_file = img_file
        self.params = read_yaml(PARAMS_FILE_PATH)
        print(self.params)


    def predict(self):
        img = (imread(self.img_file)/255).astype(np.float32)
        logger.info('image loaded successfully')
        img = resize(img,(256,256,3))
        logger.info('image resized successfully')
        img = np.array([img])

        model = load_pkl(Path('artifacts/training/trained_model.pkl'))
        result = model.predict(img)
        logger.info('Model predicted successfully')
        output_image = result[0,:]

        return output_image


    

if __name__ == '__main__':
    try:
        logger.info('Prediction pipeline started')
        obj = PredictionPipeline(Path('/home/lonewolf/noisyimage.jpeg'))
        obj.predict()
        logger.info('Prediction pipeline Completed')
    except Exception as e:
        logger.exception(e)
        raise e