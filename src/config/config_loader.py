import os
import yaml

# Function to load yaml configuration file
def load_config(config_name):
    with open(config_name, "r") as file:
        config = yaml.safe_load(file)

    return config
