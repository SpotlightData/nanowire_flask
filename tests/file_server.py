#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:28:08 2019

@author: stuart
"""

#nanowire_flask test file server

import os

from nanowire_flask.file_tools import mount_file_function

def test_file_function(filename, variables):
    
    print("RECEVED FILE REQUEST")

    with open(filename, 'r') as f:
        
        result = f.read()

    out = {"result":result.lstrip().rstrip(),
           "variables":variables}
    
    return out

#print("FOUND VERSION", nanowire_flask.__version__)

mount_file_function(test_file_function, port=5006)
