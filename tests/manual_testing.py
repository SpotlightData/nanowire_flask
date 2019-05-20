#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:49:14 2019

@author: stuart
"""

#testing the nanowire_flask library

import time
import json
import threading
import requests

from nanowire_flask.text_tools import mount_text_function


def test_text_function(text, variables):
    
    
    time.sleep(2)
    
    out = {"text":text,
           "variables":variables}
    
    return out



text_thread = threading.Thread(target = mount_text_function(test_text_function, port = 5001))
text_thread.daemon = True

text_thread.start()


text_target = 'http://192.168.129.19:5001'


d = json.dumps({"content":"Three Islamic State militants were killed while trying to escape in southwest of Kirkuk province, the pro-government Shiite paramilitary troops announced.",
                "clean_text":0,
                "deactivate_entities":0,
                "deactivate_summary":0})#, 
                #"custom_stopwords":stopwords})

heads ={"Content-Type":"application/json"}

r = requests.post(text_target, headers = heads, data=d)

