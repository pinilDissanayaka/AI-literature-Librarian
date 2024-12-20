import os 
import yaml


def load_config(config_path="config.yml")->dict:
    """
    This function reads the config file and parses it into a python dictionary
    Args:
        config_path (str): The path to the config file. Defaults to "config.yml".
    Returns:
        dict: The parsed config.
    Raises:
        FileNotFoundError: If the file is not found.
        ValueError: If the file is not a valid YAML file.
    """
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config_file=yaml.safe_load(file)

        return config_file
    except FileNotFoundError as fileNotFoundError:
        # The file is not found
        raise FileNotFoundError(f"Failed to find the config file at {config_path}, 
                                {fileNotFoundError.args}")
    except yaml.YAMLError as yamlError:
        # The file is not a valid YAML file
        raise ValueError(f"Failed to parse the config file at {config_path},
                         {yamlError.args}")
