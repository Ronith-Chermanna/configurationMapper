from config_mapper.config_manager import flatten_dict

def test_flatten_dict():
    nested_dict = {
        'server1': {
            'host': 'http://localhost',
            'port': 8084,
        },
        'server2': {
            'host': 'http://testhost'
        }
    }
    expected_flat_dict = {
        'server1_host': 'http://localhost',
        'server1_port': 8084,
        'server2_host': 'http://testhost'
    }
    assert flatten_dict(nested_dict, sep='_') == expected_flat_dict
