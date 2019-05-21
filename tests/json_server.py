#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:00:36 2019

@author: stuart
"""

#json server

import time

import nanowire_flask as nf

from nanowire_flask.json_tools import mount_json_function


def test_json_function(inputJSON):
    
    print("RECEVED REQUEST")
    
    time.sleep(1)
    
    out = inputJSON
    
    return out


print("FOUND VERSION", nf.__version__)

mount_json_function(test_json_function, port=5003)