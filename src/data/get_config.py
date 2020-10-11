import os
import yaml

# TODO Global değişkenler için de bir Config file yapılabilir ya da parametrik alınabilir bu değer
CONFIG_PATH = "../conf/"


def get_config(config_file, config_name):
    file_path = os.path.join(CONFIG_PATH, config_file)
    # read yaml file
    with open(file_path) as file:
        yaml_data = yaml.safe_load(file)

    return yaml_data[config_name]
