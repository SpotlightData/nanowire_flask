#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:18:21 2019

@author: stuart
"""

#nanowire flask setup file

from setuptools import setup

setup(
    name='nanowire_flask',
    version='0.1dev',
    description='Tool for creating nanowire tools with the flask structure.',
    url = 'https://github.com/SpotlightData/nanowire_flask',
    author='Stuart Bowe',
    author_email='stuart@spotlightdata.co.uk',
    packages=['nanowire_flask'],
    license='MIT',
    long_description=open('README.txt').read(),
)