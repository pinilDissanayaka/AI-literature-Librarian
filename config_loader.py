import os 
import yaml


def load_config(config_path="config.yml")->dict:
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config_file=yaml.safe_load(file)

        return config_file
    except FileNotFoundError as fileNotFoundError:
        raise FileNotFoundError()
    except yaml.YAMLError as yamlError:
        raise ValueError()
    


    

