#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:28:08 2019

@author: stuart
"""

#nanowire_flask test file server

import importlib
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#print(os.path.join(dir_path, '../nanowire_flask'))
#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#nanowire_flask =  importlib.import_module(os.path.join(dir_path, '../nanowire_flask'))

import nanowire_flask.file_tools

print(dir(nanowire_flask))
print(dir(nanowire_flask.file_tools))

def test_file_function(filename, variables):
    
    print("RECEVED FILE REQUEST")

    with open(filename, 'r') as f:
        
        result = f.read()

    out = {"result":result.lstrip().rstrip(),
           "variables":variables}
    
    return out

#print("FOUND VERSION", nanowire_flask.__version__)

nanowire_flask.file_tools.mount_file_function(test_file_function, port=5006)
