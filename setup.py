#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:18:21 2019

@author: stuart
"""

#nanowire flask setup file

from setuptools import setup, find_namespace_packages, find_packages


VERSION = None
with open("./nanowire_flask/VERSION") as f:
    VERSION = f.read()

includes = ['nanowire_flask', 
            'nanowire_flask.text_tools', 
            'nanowire_flask.csv_tools', 
            'nanowire_flask.file_tools',
            'nanowire_flask.image_tools',
            'nanowire_flask.json_tools']

setup(
    name='nanowire_flask',
    description='Tool for creating nanowire tools with the flask structure.',
    version=VERSION,
    keywords=['flask', 'API', 'nanowire', 'spotlight data'],
    url = 'https://github.com/SpotlightData/nanowire_flask',
    author='Stuart Bowe',
    author_email='stuart@spotlightdata.co.uk',
    packages=find_namespace_packages(exclude=['tests'], include=includes),
    license='MIT',
    long_description=open('README.md').read(),
    long_destription_content_type='text/markdown',
    include_package_data=True,
    package_data={
        'data':['./nanowire_flask/VERSION']
    },
    data_files = [('', ['./nanowire_flask/VERSION'])],
    install_requires=[
	'Pillow>=5.4.1',
	'requests>=2.21.0',
	'Flask-API>=1.1',
	'jsonpickle>=1.1',
	'psutil>=5.5.0',
    'pandas>=0.23.4',
    'xlrd>=1.0.0']
)