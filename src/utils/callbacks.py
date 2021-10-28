from utils.all_utils import get_timestamp

import os
import tensorflow as tf
import joblib
import logging

    
def  create_and_save_tensorboard_callbacks(callbacks_dir,tensorboard_log_dir):
    unique_name = get_timestamp("tb_logs")

    tb_tensorboard_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_tensorboard_log_dir)

    tb_callback_filepath = os.path.join(callbacks_dir, "tensorboard_cb.cb")
    joblib.dump(tensorboard_callback,tb_callback_filepath)

    logging.info(f"Tensorflow Callback saved at following path {tb_callback_filepath}")

def create_and_save_checkpoints_callbacks(callbacks_dir,checkpoint_dir):
    checkpoint_file_path = os.path.join(checkpoint_dir, "ckpt_model.h5")
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath= checkpoint_file_path, 
        save_best_only=True
    )

    ckpt_callback_filepath = os.path.join(callbacks_dir, "checkpoint_cb.cb")
    joblib.dump(checkpoint_callback,ckpt_callback_filepath)

    logging.info(f"Checkpoint Callback saved at following path {ckpt_callback_filepath}")
