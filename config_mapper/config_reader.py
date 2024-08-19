import yaml
from configparser import  ConfigParser


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def read_cfg(file_path):
    config = ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}


def read_conf(file_path):
    # Sometimes configparser fails, So manual parsing is enabled in exceptions
    try:
        return read_cfg(file_path)
    except Exception:
        return manually_read_config(file_path)


def manually_read_config(file_path):
    config_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_key = None
    for line in lines:
        line = line.strip()
        if line.startswith('#') or not line:
            continue  # This Skips comments and empty lines
        if '{' in line:
            current_key = line.split()[0]
            config_dict[current_key] = {}
        elif '}' in line:
            current_key = None
        else:
            if current_key:
                key_value = line.split()
                config_dict[current_key][key_value[0]] = key_value[1] if len(key_value) > 1 else None

    return config_dict
