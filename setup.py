'''
Build script for package's wheel and zip files. 

Look in the `dist` folder for the output. 

Usage: 
    Run as follows: 
    >python setup.py sdist --formats=zip bdist_wheel
'''
from pathlib import Path

import json
import os
import setuptools
import shutil
import sys
from platform import python_revision

def cleanup(package_dict):
    shutil.rmtree('./build', ignore_errors=True)
    shutil.rmtree('[].egg-info'.format(package_dict['name']), 
                  ignore_errors=True)
    shutil.rmtree('./src/{}.egg-info'.format(package_dict['name']), 
                  ignore_errors=True)


package_dict = {'name': '', '__version__': '', '__author__': ''}
init_path = Path("src") / 'pdf_utils' / '__init__.py' 
print('Retrieved the following settings from __init__.py')
with open(init_path) as init:
    for line in init: 
        for key in package_dict: 
            if line.startswith(f'{key} = '): 
                package_dict[key] = line.split('=')[1].strip().strip("\"'")
                print(f'  >> {key}: {package_dict[key]}')

cleanup(package_dict)  # remove previous build cruft

with open('README.md') as fh: 
    long_description = fh.read()

dependencies = setuptools.find_packages('src')
print('Package dependencies: {}'.format(dependencies))

with open('requirements.txt') as fh: 
    requirements = fh.read().splitlines()
print('Package requirements: {}'.format(requirements))

setuptools.setup(
    name = package_dict['name'],
    version = package_dict['__version__'],
    author = package_dict['__author__'],
    description = 'PDF utility classes',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/gismaps/PDF_Utils', 
    packages = dependencies,
    install_requires = requirements, 
    package_dir = {'': 'src'},
    data_files = [],   # [('license', ['LICENSE.txt'])], # done via MANIFEST.in
    include_package_data = True,
    license = "MIT",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    python_requires = '>=3.6',
    )

cleanup(package_dict)  # remove build cruft

print('setup.py ended normally')

