#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:12:51 2019

@author: stuart
"""

#nanowire flask plugin tool



import time
from PIL import Image

import requests

from io import BytesIO

import traceback

import jsonpickle
from flask import request, Response
from flask.views import View

from flask_api import FlaskAPI

import inspect

def run_image(r, app): 
 
    start_time = time.time()

    #if the user has sent a url then we want to extract that URL like this
    if r.headers['Content-Type'] != 'application/json':
    
        variables_info = dict(r.values)
                
        # convert string of image data to uint8
        im = Image.open(r.files['image']).convert("RGB")

    #if the user has sent an image then lets extract that image and store it as
    #a PIL
    else:
        #extract the variables info sent to the plugin
        variables_info = r.json
        
        #extract the image from the sent url
        im_request = requests.get(variables_info['contentUrl'])
        im = Image.open(BytesIO(im_request.content)).convert("RGB")

    #apply the function to the image
    out_predictions = app.config['function'](im, variables_info)
    
    print("Took {0:0.2f} seconds".format(time.time()-start_time))
    
    return out_predictions

#function to check if the user defined function is as it should be
def check_function_is_valid(function):

    args = inspect.getargspec(function)[0]

    if args != ['img', 'variables'] and args != ['self', 'img', 'variables'] and args != ['img'] and args != ['self', 'img']:
        
        return False
        
    else:
        return True


class mount_Image_function(object):
    
    def __init__(self, function, debug_mode=False, host='0.0.0.0', port=5000, path='/model/predict'):
        
        self.app = FlaskAPI(__name__)

        self.app.config['debug'] = debug_mode
        
        self.app.config['function'] = function
        
        self.host = host
        
        self.port = port
        
        self.path = path
        
        if check_function_is_valid(self.app.config['function']):
            
            #define the class we're mounting onto post
            tool = ImagesAPI
            
            #store a link to the app in tool
            tool.app = self.app
            
            #create the rule for /model/predict
            self.app.add_url_rule(self.path, view_func = tool.as_view('UserAPI'))
            
            #run the app
            self.app.run(host=self.host, port=self.port, debug=self.app.config['debug'])
        
        else:
            #if the function has bad inputs reject it
            raise Exception("BAD ARGUMENTS SENT TO FUNCTION")

    
class ImagesAPI(View):
    
    methods = ['POST']
    
    def dispatch_request(self):
        
        try:
            answer = run_image(request, self.app)
            
            if not isinstance(answer, dict):
                
                raise Exception("PLUGIN MUST RETURN A DICTIONARY, RETURNED {0}".format(str(type(answer))))
            
            answer['status'] = 'ok'
            
            response_pic = jsonpickle.encode(answer)
            #everything has gone fine, return the results in a nice response
            return Response(response=response_pic, status=200, mimetype="application/json")
        
        except Exception as exp:
            

            response = {'status':'failure', 'error':str(exp)}
            
            #if we're in debug mode then return a full traceback
            if self.app.config['debug']:
                response['full_traceback'] = str(traceback.format_exc())
                
            response_pic = jsonpickle.encode(response)
            
            #something has gone wrong return the bad result in this response
            return Response(response=response_pic, status=400, mimetype='application/json')

