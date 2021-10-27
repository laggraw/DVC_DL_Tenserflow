from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import get_VGG_16_model
import argparse
import shutil
import logging
import pandas as pd
from tqdm import tqdm
import os



def prepare_base_model(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config['artifacts']
    artifacts_dir = artifacts['ARTIFACTS_DIR']

    base_model_dir = artifacts['BASE_MODEL_DIR']
    base_model_name = artifacts['BASE_MODEL_NAME']
    updated_base_model_name = artifacts['UPDATED_BASE_MODEL_NAME']

    base_model_dir_path = os.path.join(artifacts_dir,base_model_dir)
    create_directory([base_model_dir_path])
    base_model_path = os.path.join(base_model_dir_path,base_model_name)

    model = get_VGG_16_model(input_shape =params["IMAGE_SIZE"], model_path = base_model_path)




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-c", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>>>>>>>>>Stage 02 started>>>>>>>>>>>>>")
        prepare_base_model(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info(">>>>>>>>>>>>>Stage 02 completed, Base model is created>>>>>>>>>>>>>")
    except Exception as e : 
        logging.exception(e)
        raise e
