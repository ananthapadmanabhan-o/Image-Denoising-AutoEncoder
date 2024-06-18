import os 
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import yaml
from denoisingEncoder import logger


@ensure_annotations
def read_yaml(yaml_path:Path) -> ConfigBox:
    '''
    Args:
        yaml_path (Path)
    
    Returns:
        ConfigBox of contents inside yaml file

    '''
    try:
        with open(yaml_path) as yaml_file:
            contents = yaml.safe_load(yaml_file)
            logger.info(f'yaml file {yaml_path} loaded successfully')

            return ConfigBox(contents)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(dir_path:list):
    '''create list of directories
    
    Args:
        dir_path (list): list of directories to be created
    '''
    for path in dir_path:
        os.makedirs(path,exist_ok=True)
        logger.info(f'created directory in path {path}')