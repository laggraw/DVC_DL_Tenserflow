from keras_preprocessing.image.image_data_generator import ImageDataGenerator
import tensorflow as tf
import logging


def train_valid_generator(data_dir, IMAGE_SIZE, BATCH_SIZE, do_data_agumentation):
    datagenerator_kwargs = dict(
        rescale = 1./255,
        validation_split = 0.25,
        
    )

    dataflow_kwargs = dict(
        target_size = IMAGE_SIZE,
        batch_size = BATCH_SIZE,
        interpolation = "bilinear"

    )

    valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

    valid_generator = valid_datagenerator.flow_from_directory(
        directory = data_dir,
        subset = "validation",
        shuffle= False,
        **dataflow_kwargs
    )

    if do_data_agumentation :
        train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range= 40,
            horizontal_flip= True,
            width_shift_range= 0.2,
            height_shift_range= 0.2,
            shear_range= 0.2,
            zoom_range = 0.2, **datagenerator_kwargs
        )
        logging.info("Data agumentaion is done for training data")
    else:
        train_datagenerator = valid_datagenerator
        logging.info("Data agumentaion is NOT done for training data")

    train_generator = train_datagenerator.flow_from_directory(
        directory = data_dir,
        subset= "training",
        shuffle = True,
        **dataflow_kwargs
    )

    logging.info("Train and Valid generator Created.")
    return train_generator,valid_generator