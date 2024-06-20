from denoisingEncoder.utils.common import load_pkl,read_yaml,create_directories
from denoisingEncoder.constants import PARAMS_FILE_PATH,CONFIG_FILE_PATH
from pathlib import Path
from skimage.io import imread
import matplotlib.pyplot as plt 
from skimage.transform import resize
import numpy as np
from denoisingEncoder import logger



class PredictionPipeline:
    def __init__(self,img_file):
        self.img_file = img_file
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)


    def predict(self):
        img = (imread(self.img_file)/255).astype(np.float32)
        logger.info('image loaded successfully')
        img = resize(img,(self.params.IMAGE_WIDTH,self.params.IMAGE_HEIGHT,self.params.IMAGE_CHANNEL))
        logger.info('image resized successfully')
        img = np.array([img])

        model = load_pkl(Path('assets/model/model.pkl'))
        result = model.predict(img)
        logger.info('Model predicted successfully')
        output_image = result[0,:]

        create_directories([self.config.predict.root_dir])

        with open(Path(self.config.predict.output_image_path),'wb') as file:
            plt.imsave(file,output_image)

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