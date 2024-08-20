import pytest
from config_mapper.utils import get_file_handler, get_write_handler

def test_get_file_handler_yaml():
    handler = get_file_handler('yaml')
    assert handler is not None
    assert callable(handler)

def test_get_file_handler_cfg():
    handler = get_file_handler('cfg')
    assert handler is not None
    assert callable(handler)

def test_get_file_handler_conf():
    handler = get_file_handler('conf')
    assert handler is not None
    assert callable(handler)

def test_get_file_handler_invalid():
    handler = get_file_handler('invalid')
    assert handler is None

def test_get_write_handler_json():
    handler, output_file = get_write_handler('json')
    assert handler is not None
    assert callable(handler)
    assert output_file == 'configs.json'

def test_get_write_handler_os():
    handler, output_file = get_write_handler('os')
    assert handler is not None
    assert callable(handler)
    assert output_file is None

def test_get_write_handler_env():
    handler, output_file = get_write_handler('env')
    assert handler is not None
    assert callable(handler)
    assert output_file == '.env'

def test_get_write_handler_invalid():
    handler, output_file = get_write_handler('invalid')
    assert handler is None
    assert output_file is None
