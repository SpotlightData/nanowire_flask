#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:28:08 2019

@author: stuart
"""

#run text server

import time
import json
import threading
import requests

import nanowire_flask as nf

from nanowire_flask.text_tools import mount_text_function


def test_text_function(text, variables):
    
    print("RECEVED REQUEST")
    
    time.sleep(1)
    
    out = {"text":text,
           "variables":variables}
    
    return out


print("FOUND VERSION", nf.__version__)

mount_text_function(test_text_function, port=5000)
