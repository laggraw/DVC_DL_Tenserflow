from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import get_VGG_16_model,prepare_model
import argparse
import io
import logging
import os

logging_str = "[%(asctime)s : %(levelname)s : %(module)s] : %(message)s"
log_dirs = "logs"
os.makedirs(log_dirs, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dirs, "running_logs.log"), 
level= logging.INFO,format= logging_str, filemode= 'a' )


def prepare_callbacks(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>>>>>>>>>Stage 03 started>>>>>>>>>>>>>")
        prepare_callbacks(config_path=parsed_args.config,params_path=parsed_args.params) 
        logging.info(">>>>>>>>>>>>>Stage 03 completed, prepare callbacks is completed and saved as binary file>>>>>>>>>>>>>")
    except Exception as e : 
        logging.exception(e)
        raise e