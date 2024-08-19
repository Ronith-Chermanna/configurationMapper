from config_mapper.config_reader import read_yaml, read_cfg, read_conf
from config_mapper.config_writer import set_env_variables, write_to_env, write_to_json

file_handlers = {
    'yaml': read_yaml,
    'cfg': read_cfg,
    'conf': read_conf
}


def get_file_handler(file_extension):
    return file_handlers.get(file_extension)

write_handlers = {
    'os': (set_env_variables, None),
    'env': (write_to_env, '.env'),
    'json': (write_to_json, 'configs.json')
}


def get_write_handler(write_format):
    return write_handlers.get(write_format, (None, None))
