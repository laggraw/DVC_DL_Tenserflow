from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import load_full_model
from src.utils.callbacks import get_callbacks
from src.utils.data_management import train_valid_generator
import argparse
import logging
import os

logging_str = "[%(asctime)s : %(levelname)s : %(module)s] : %(message)s"
log_dirs = "logs"
os.makedirs(log_dirs, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dirs, "running_logs.log"), 
level= logging.INFO,format= logging_str, filemode= 'a' )

def train_model(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config['artifacts']
    artifacts_dir = artifacts['ARTIFACTS_DIR']

    train_model_dir_path = os.path.join(artifacts_dir, artifacts['TRAINED_MODEL_DIR'])
    create_directory([train_model_dir_path])

    untrained_full_model_path = os.path.join(artifacts_dir, artifacts['BASE_MODEL_DIR'], artifacts['UPDATED_BASE_MODEL_NAME'])
    
    model = load_full_model(untrained_full_model_path)

    callback_dir_path = os.path.join(artifacts_dir, artifacts['CALLBACKS_DIR'] )

    callbacks = get_callbacks(callback_dir_path)


    train_generator, valid_generator = train_valid_generator(

        data_dir = artifacts['DATA_DIR'],
        IMAGE_SIZE = tuple(params['IMAGE_SIZE'][:-1]),
        BATCH_SIZE = params['BATCH_SIZE'],
        do_data_agumentation = params['AGUMENTATION']
    )

    steps_per_epochs = train_generator.samples // train_generator.batch_size
    validation_steps = valid_generator.samples // valid_generator.batch_size

    model.fit(
        train_generator,
        validation_data = valid_generator, 
        epochs = params["EPOCHS"], 
        steps_per_epoch = steps_per_epochs,
        validation_steps = validation_steps,
        callbacks = callbacks
        )

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>>>>>>>>>Stage 04 started>>>>>>>>>>>>>")
        train_model(config_path=parsed_args.config,params_path=parsed_args.params) 
        logging.info(">>>>>>>>>>>>>Stage 04 completed, training completed and model saved>>>>>>>>>>>>>\n")
    except Exception as e : 
        logging.exception(e)
        raise e