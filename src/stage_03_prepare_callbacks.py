from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import get_VGG_16_model,prepare_model
from src.utils.callbacks import create_and_save_tensorboard_callbacks,create_and_save_checkpoints_callbacks
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

    artifacts = config['artifacts']
    artifacts_dir = artifacts['ARTIFACTS_DIR']

    tensorboard_log_dir = os.path.join(artifacts_dir, artifacts['TENSORBOARD_ROOT_LOG_DIR'])
    checkpoint_dir = os.path.join(artifacts_dir, artifacts['CHECKPOINT_DIR'])
    callbacks_dir = os.path.join(artifacts_dir, artifacts['CALLBACKS_DIR'])

    create_directory([tensorboard_log_dir,checkpoint_dir,callbacks_dir])

    create_and_save_tensorboard_callbacks(callbacks_dir,tensorboard_log_dir)
    create_and_save_checkpoints_callbacks(callbacks_dir,checkpoint_dir)

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