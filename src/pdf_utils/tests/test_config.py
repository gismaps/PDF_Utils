"""
This file is configuration for the unit tests. It contains one item,
a dict named `test_config`. Import it like this: 

```from pdf_utils.tests import test_config```
"""

test_config = {
    'inputs': {
        'levels_to_root': 4, # folders down from root, including test .py file
        'test_data_path': 'data/tests',  # Relative to project root
        'pdf1': 'pages_odd.pdf',
        'pdf1_len': 5,
        'pdf2': 'pages_even.pdf',
        },
    'outputs': {
        'path': '/temp', # absolute path
        }
    }

if __name__ == '__main__':
    print("Import this config file, rather than executing it:")
    print('from pdf_utils.tests.test_config import test_config')
