from src.utils.all_utils import read_yaml, create_directory
import argparse
import shutil
import logging
import pandas as pd
import tqdm
import os


def get_data(config_path):
    config = read_yaml(config_path)

    source_download_paths = config['source_download_paths']
    local_data_path = config['local_data_path']



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path="config/config.yaml")
