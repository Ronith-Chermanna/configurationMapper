import json
import os


def write_to_env(config_dict, output_file):
    with open(output_file, 'w') as file:
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")


def write_to_json(config_dict, output_file):
    with open(output_file, "w") as file:
        json.dump(config_dict, file, indent=4)


def set_env_variables(config_dict):
    for key, value in config_dict.items():
        os.environ[key] = str(value)
