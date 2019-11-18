#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:12:51 2019

@author: stuart
"""

#nanowire flask plugin tool

import time
from PIL import Image

import unicodedata as uni

import requests

from io import BytesIO

import traceback

import jsonpickle
from flask import request, Response
from flask.views import View

from flask_api import FlaskAPI

import pandas as pd

#memory and cpu usage collection tools

import sys
import os
import re
import psutil
import threading
import socket

py_version = int(sys.version[0])


if py_version == 2:
    import Queue as queue
else:
    import queue


import inspect

import logging

logging.basicConfig(format='%(message)s')

logger = logging.getLogger('NANOWIRE_FLASK_TOOL')

logger.setLevel(level=logging.DEBUG)

mod_path = os.path.abspath(__path__[0])

files = os.listdir(os.path.join(mod_path, '../../'))

files[:] = [x for x in files if 'nanowire_flask' in x]

files[:] = [x for x in files if x != 'nanowire_flask']

print("FILES")
print(mod_path)
print(files)
print(os.listdir(mod_path))
print("+++++++++++++++++++++++++++++++++")

try:
    __version__ = re.findall(r'([0-9]*\.[0-9]*\.[0-9]*)', files[0])[0]
except:
    if 'VERSION' in os.listdir(mod_path):
        with open(os.path.join(mod_path, 'VERSION'), 'r') as f:
            __version__ = f.read()
    else:
        __version__ = 'unknown'


print("NANOWIRE_FLASK VERSION", __version__)

###################
### Admin tools ###
###################

def scrub_newlines(txt):
    
    out = ""
    for char in txt:
        if uni.category(char) != "Cc":
            
            out += char
            
    return out

##############################
### ADVANCED LOGGING TOOLS ###
##############################

class usage_collection(object):
    
    def __init__(self):
        

        #CPUs are collected in % usage
        self.cpus_queue = queue.Queue()
        #memory queue is in MB
        self.mem_queue = queue.Queue()
        self.running = False
    
    def collection_thread(self):
        
        #logger.info("Background thread is STARTING")
        self.running = True
        
        while self.running:
            
            self.cpus_queue.put_nowait(psutil.cpu_percent())
            self.mem_queue.put_nowait(psutil.Process(os.getpid()).memory_info().rss/1e6)
            time.sleep(0.01)
            #logger.info("Background thread is RUNNING")
            
        #logger.info("Background thread is CLOSING")
            
            
    def finish_collection(self):
        
        self.running = False

        cpus = []
        mems = []
        while True:
            try:
                cpus.append(self.cpus_queue.get_nowait())
                mems.append(self.mem_queue.get_nowait())

            except:
                break
        if len(mems) > 0:
        
            max_mem = max(mems)
            max_cpu = max(cpus)
            
        else:
            max_mem = psutil.Process(os.getpid()).memory_info().rss/1e6
            max_cpu = psutil.cpu_percent()
            
        return [max_mem, max_cpu]
    
    def start_collection(self):
        
        threading.Thread(target=self.collection_thread).start()
