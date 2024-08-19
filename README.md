# Configuration Mapper

`config_mapper` is a Python package that helps you read, process, and write configuration files in various formats. It supports YAML, CFG, and CONF formats, and can output configurations to environment variable file, JSON files, or directly set them in the OS environment.

## Installation

You can install the package directly from your Git repository using either HTTP or SSH.

### HTTP Installation Or SSH Installation

```bash
pip install git+https://github.com/Ronith-Chermanna/configurationMapper.git@main
OR
pip install git+ssh://git@github.com:Ronith-Chermanna/configurationMapper.git@main
```
### Usage
```bash
from config_mapper.config_manager import process_config

# Example usage: process_config returns a flat dictionary
config_dict = process_config(file_path="path/to/your/config.yaml")

```
### Calling process_config
```bash
process_config(
    file_path, 
    output_format="", 
    separator="_", 
    output_path=""
)
```
Parameters
file_path (mandatory):

    The path to the configuration file. This file can be in .yaml, .cfg, or .conf format.

output_format (optional, default is ""):

    Specifies the format in which to output the flattened configuration dictionary:
        "json": Outputs the flattened dictionary as a JSON file.
        "env": Writes the flattened dictionary to a .env file.
        "os": Sets the flattened dictionary as environment variables in the current OS environment.
        "" (default): Returns the flattened dictionary without writing to any file.

separator (optional, default is "_"):

    The separator used to flatten nested dictionary keys. By default, it uses an underscore (_),  but you can customize this to any other character(s) you prefer.

output_path (optional, default is the current working directory):

    The path where the output file will be saved:
    If output_format is "json", the output will be saved as config.json.
    If output_format is "env", the output will be saved as .env.
    If output_format is "os", output_path is not used.
    If no output_path is provided, the file will be written to the current working directory.
    If an output_path is provided, the output file will be saved to the specified directory or file path.

### Sample
###Example: Flatten a YAML configuration file and write it to a JSON file

config_dict = process_config(
    file_path="path/to/your/config.yaml", 
    output_format="json",
    output_path="path/to/output/config.json"
)
