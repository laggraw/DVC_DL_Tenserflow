from src.utils.all_utils import read_yaml, create_directory
import argparse
import shutil
import logging
import pandas as pd
from tqdm import tqdm
import os

def copy_file(src, dest):
    list_of_files = os.listdir(src)
    N = len(list_of_files)
    for file in tqdm(list_of_files, total = N, desc= f'Copying file for {src} to {dest}', color = 'green' ):
        src_file = os.path.join(src, file)
        dest_file = os.path.join(dest, file)
        shutil.copy(src_file, dest_file)

def get_data(config_path):
    config = read_yaml(config_path)

    source_download_dirs = config['source_download_dirs']
    local_data_dirs = config['local_data_dirs']

    create_directory([local_data_dirs])
    for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs,local_data_dirs), total = 2, desc = "List of folder", color = 'orange'):
        copy_file(source_download_dir,local_data_dir)





if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path="config/config.yaml")
