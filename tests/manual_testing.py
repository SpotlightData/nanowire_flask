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
import os
import unittest
import qrcode

import pandas as pd


from http.server import HTTPServer, SimpleHTTPRequestHandler


#test the text processing tools
class text_server_test_case(unittest.TestCase):
    
    def test_text_json_example(self):

        
        text_target = 'http://192.168.128.19:5000/model/predict'
        
        
        d = json.dumps({"text":"Example of text.",
                        "clean_text":0,
                        "deactivate_entities":0,
                        "deactivate_summary":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()
        
        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example of text.")
        
    
    def test_text_file_example(self):
        
        text_target = 'http://0.0.0.0:5000/model/predict'
        
        files = {'doc': ('./test_text1.txt', open('./test_text1.txt', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.1', files=files)
        
        out = r.json()
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('threshold' in out['variables'].keys())
        
        with open('./test_text1.txt', "r") as f:
            t = f.read()
        
        self.assertTrue(out['text'] == t)
        
        
    def test_text_from_server(self):
        
        text_target = 'http://0.0.0.0:5000/model/predict'
        
        text_file = 'http://0.0.0.0:8001/test_text1.txt'
        
        d = json.dumps({"contentUrl":text_file,
                        "clean_text":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()
                
        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        
        with open('./test_text1.txt', "r") as f:
            t = f.read()
        
        self.assertTrue(out['text'] == t)
    
#test the image processing tools
class image_server_test_case(unittest.TestCase):
    
    def test_from_file_png(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        files = {'image': ('./example_qr_code.png', open('./example_qr_code.png', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.5', files=files)
        
        out = r.json()
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
    def test_from_file_jpg(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        files = {'image': ('./example_qr_code.jpg', open('./example_qr_code.jpg', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.5', files=files)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
    def test_from_file_jpeg(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        files = {'image': ('./example_qr_code.jpeg', open('./example_qr_code.jpeg', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.5', files=files)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
    def test_from_file_bmp(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        files = {'image': ('./example_qr_code.bmp', open('./example_qr_code.bmp', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.5', files=files)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
        
    def test_from_server_png(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        image_url = 'http://0.0.0.0:8001/example_qr_code.png'
        
        d = json.dumps({"contentUrl":image_url,
                "clean_text":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
        
    def test_from_server_jpg(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        image_url = 'http://0.0.0.0:8001/example_qr_code.jpg'
        
        d = json.dumps({"contentUrl":image_url,
                "clean_text":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
          
    def test_from_server_jpeg(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        image_url = 'http://0.0.0.0:8001/example_qr_code.jpeg'
        
        d = json.dumps({"contentUrl":image_url,
                "clean_text":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
    def test_from_server_bmp(self):
        
        text_target = 'http://0.0.0.0:5001/model/predict'
        
        image_url = 'http://0.0.0.0:8001/example_qr_code.bmp'
        
        d = json.dumps({"contentUrl":image_url,
                "clean_text":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['text'] == "Example image")
        
#test the csv processing tools
class csv_server_test_case(unittest.TestCase):
    
    def test_from_file_csv(self):
        
        text_target = 'http://0.0.0.0:5002/model/predict'
        
        files = {'csv': ('./example.csv', open('./example.csv', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.5', files=files)
        
        out = r.json()
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['shape'] == [2, 3])
        
    def test_from_server_csv(self):
        
        text_target = 'http://0.0.0.0:5002/model/predict'
        
        csv_url = 'http://0.0.0.0:8001/example.csv'
        
        d = json.dumps({"contentUrl":csv_url,
                "clean_text":1})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['shape'] == [2, 3])

        
        
####################################
### End of unit test definitions ###
####################################
        
        
#generate pngs, jpgs and bmps of qr codes to test the image server
img = qrcode.make("Example image")

img.save('example_qr_code.png')
img.save('example_qr_code.jpg')
img.save('example_qr_code.jpeg')
img.save('example_qr_code.bmp')
        
#generate the csvs for testing the csv server
df_dict = {'uuid':['t-001', 't-002', 't-003'], 'texts':['example', 'text', 'No3']}

example_df = pd.DataFrame(df_dict)

example_df.to_csv('example.csv', index=False)

#start the file hosting server
httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
    
base_serve_thread = threading.Thread(name='s1', target=httpd.serve_forever, daemon = True)

base_serve_thread.start()

print("STARTING TEXT SERVER")
#start the text server
run_text_cmd = 'python3 ./text_server.py &'

result = os.system(run_text_cmd)

print("STARTING IMAGE SERVER")

run_img_cmd = 'python3 ./image_server.py &'

result = os.system(run_img_cmd)

run_csv_cmd = 'python3 ./csv_server.py &'

result = os.system(run_csv_cmd)

print("STARTING CSV SERVER")

#wait for the server to start
time.sleep(5)

#perform the unit tests
unittest.main()
#text_thread.exit()




