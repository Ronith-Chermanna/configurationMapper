from config_mapper.utils import get_file_handler, get_write_handler


def flatten_dict(comfig_dict, sep, parent_key=''):
    items = {}
    for k, v in comfig_dict.items():
        if '=' in k:
            prefix, new_key = k.split('=', 1)
        else:
            new_key = k
        new_key = f"{parent_key}{sep}{new_key}" if parent_key else new_key

        if isinstance(v, dict):
            items.update(flatten_dict(comfig_dict=v, sep=sep, parent_key=new_key))
        else:
            items[new_key] = v
    return items


def read_config(file_path):
   file_extension = file_path.split('.')[-1]
   handler = get_file_handler(file_extension)

   if handler:
       return handler(file_path=file_path)
   else:
       raise ValueError(f"Unsupported File format: {file_extension}")


def process_config(file_path, output_format="", seperator="_", output_path=""):
    config_dict = read_config(file_path=file_path)
    config_dict = flatten_dict(comfig_dict=config_dict, sep=seperator)

    handler, default_output_file = get_write_handler(write_format=output_format)
    if not output_path:
        output_path = default_output_file
    if handler:
        handler(config_dict=config_dict, output_file=output_path)

    return config_dict
