# this file will be responsible for reading configuration files and providing configuration data to the rest of the application

import json
import yaml
from pathlib import Path

def run(args):
    config = ConfigurationManager()
    print("Configuration module selected")
    print("\nJSON Configuration")
    print(config.load_json_config())
    print("\nYAML Configuration")
    print(config.load_yaml_config())

class ConfigurationManager:
    # constructor
    def __init__(self):
        # creates a Path object pointing to the config/ directory
        self.config_dir = Path("config")
        # creates the paths
        self.json_config = self.config_dir / "config.json"
        self.yaml_config = self.config_dir / "config.yaml"

    def load_json_config(self):
        # opens the config.json file in read mode
        # converts json into a python dictionary
        # if config.json does not exits, the program won't crash, it prints an error and returns an empty dictionary
        # if json syntax is incorrect, it reports issue instead of terminating unexpectedly
        # returning an empty dictionary allows the rest of the application to continue running safely, even if configuration file is missing or invalid
        try: 
            with open(self.json_config, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.json_config} not found.")
            return{}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.json_config}.")
            return{}

    def load_yaml_config(self):
        # opens the config.yaml file in read mode
        # converts yaml into a python dictionary
        # if config.yaml does not exits, the program won't crash, it prints an error and returns an empty dictionary
        # if yaml syntax is incorrect, it reports issue instead of terminating unexpectedly
        # returning an empty dictionary allows the rest of the application to continue running safely, even if configuration file is missing or invalid
        try:
            with open(self.yaml_config, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: {self.yaml_config} not found.")
            return {}
        except yaml.YAMLError:
            print(f"Error: Invalid YAML in {self.yaml_config}.")
            return {}


