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
from pprint import pprint

from http.server import HTTPServer, SimpleHTTPRequestHandler

import functools

os.environ['PYTHON_DEBUG'] = 'True'
class test_image_server_test_case_cmd_line(unittest.TestCase):
    
    def test_img_cmd_line_send_file_direct(self):
        
        img_target = 'http://0.0.0.0:5001/model/predict'
        
        post_cmd = 'curl -F "image=@./example_qr_code.png" -XPOST ' + img_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
        
        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example image")

    def test_img_cmd_line_send_file_direct_malformed_json(self):
        
        img_target = 'http://0.0.0.0:5001/model/predict'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\"::\"urlExample, \"threshold\":0.5}'"
            
        post_cmd += ' '
        post_cmd += img_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)

        self.assertTrue('error' in out.keys())
        self.assertTrue(out['error'] == 'VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY')
        
    def test_img_cmd_line_send_file_direct_malformed_url(self):
        
        img_target = 'http://0.0.0.0:5001/model/predict'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"http://0.0.0.0:9999:/blah/blak\"}'"
            
        post_cmd += ' '
        post_cmd += img_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)

        self.assertTrue('error' in out.keys())
        self.assertTrue(out['error'] == 'COULD NOT PULL FROM URL, PLEASE CHECK URL AND RETRY')

        
class test_csv_server_cmd_line(unittest.TestCase):
    
    def test_csv_cmd_line_sent_file_direct(self):
        
        img_target = 'http://0.0.0.0:5002/model/predict'
        
        post_cmd = 'curl -F "csv=@./example.csv" -XPOST ' + img_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['shape'] == [2, 3])
        
    def test_xlsx_cmd_line_sent_file_direct(self):
        
        img_target = 'http://0.0.0.0:5002/model/predict'
        
        post_cmd = 'curl -F "xlsx=@./example.xlsx" -XPOST ' + img_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['shape'] == [2, 3])
        
    def test_xlsx_cmd_line_bad_file_url(self):
        
        post_cmd = 'curl -X POST -H "Content-Type:application/json" -d \'{"contentUrl":"http://0.0.0.0:8029/example.csv", "ignore_col":"dates"}\' http://0.0.0.0:5002/model/predict'
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
        

        self.assertTrue(out['error'] == "CANNOT CONNECT TO FILE URL, CHECK FILE URL AND TRY AGAIN")
        
    def test_xlsx_cmd_line_malformed_json(self):
        
        post_cmd = 'curl -X POST -H "Content-Type:application/json" -d \'{"contentUrl"::"http://0.0.0.0:8001/example.csv", "ignore_col":"dates"}\' http://0.0.0.0:5002/model/predict'
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
        
        self.assertTrue(out['error'] == "VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY")
        
class test_json_server_cmd_line(unittest.TestCase):
    
    def test_json_send_from_server(self):
        
        json_target = 'http://0.0.0.0:5003/model/predict'
        
        json_source = 'http://0.0.0.0:8001/example.json'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"%s\"}' %s"%(json_source, json_target)

        out = os.popen(post_cmd).read()

        out = json.loads(out)
        
        self.assertTrue(out['inputJSON']['a'] == [1, '2', True])
        self.assertTrue(out['inputJSON']['example'] == 'of')
        self.assertTrue(out['inputJSON']['json']['loaded'] == 'in')
        self.assertTrue(out['inputJSON']['json']['to'] == 'be')
    
    
    def test_json_bad_url(self):
        
        json_target = 'http://0.0.0.0:5003/model/predict'
        
        json_source = 'http://0.0.0.0:8045/example.json'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"%s\"}' %s"%(json_source, json_target)

        out = os.popen(post_cmd).read()

        out = json.loads(out)

        self.assertTrue(out['error'] == "CANNOT CONNECT TO FILE URL {0}, CHECK FILE URL AND TRY AGAIN".format(json_source))
        
        
    def test_json_malformed_json(self):
        
        json_target = 'http://0.0.0.0:5003/model/predict'
        
        json_source = 'http://0.0.0.0:8001/example.json'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\"::\"%s\"}' %s"%(json_source, json_target)

        out = os.popen(post_cmd).read()

        out = json.loads(out)
        
        self.assertTrue(out['error'] == "VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY")
        
        
    def test_json_with_variables(self):
        
        json_target = 'http://0.0.0.0:5003/model/predict'
        
        json_source = 'http://0.0.0.0:8001/example.json'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"%s\", \"customStops\":[\"horse\", \"course\"]' %s"%(json_source, json_target)

        out = os.popen(post_cmd).read()

        out = json.loads(out)
        
        self.assertTrue(out['error'] == "VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY")

#################################
### TEST FUNCTION VALIDATAION ###
#################################

class testing_function_validation(unittest.TestCase):
    
    def test_text_function_validation(self):
        
        from nanowire_flask.text_tools import check_text_function_is_valid
        
        
        def pass_function_text_no_var(text):
            
            return {}
        
        def pass_function_text_var(text, variables):
            
            return {}
        
        def fail_function_var(variables):
            
            return {}
        
        class validation_text_tester(object):
            
            def pass_function_self_text(self, text):
                
                return {}
            
            def pass_function_self_text_var(self, text, variables):
                
                return {}
            
            def fail_function_self_var(self, variables):
                
                return {}
            
        self.assertTrue(check_text_function_is_valid(pass_function_text_no_var))            
        
        self.assertTrue(check_text_function_is_valid(pass_function_text_var))
        
        self.assertTrue(not check_text_function_is_valid(fail_function_var))
        
        tester = validation_text_tester()
        
        self.assertTrue(check_text_function_is_valid(tester.pass_function_self_text))
        
        self.assertTrue(check_text_function_is_valid(tester.pass_function_self_text_var))
        
        self.assertTrue(not check_text_function_is_valid(tester.fail_function_self_var))
        
        
        
    def test_image_function_validation(self):
        
        from nanowire_flask.image_tools import check_Image_function_is_valid
        
        
        def pass_function_img_no_var(img):
            
            return {}
        
        def pass_function_img_var(img, variables):
            
            return {}
        
        def fail_function_var(variables):
            
            return {}
        
        class validation_image_tester(object):
            
            def pass_function_self_img(self, img):
                
                return {}
            
            def pass_function_self_img_var(self, img, variables):
                
                return {}
            
            def fail_function_self_var(self, variables):
                
                return {}
            
        self.assertTrue(check_Image_function_is_valid(pass_function_img_no_var))            
        
        self.assertTrue(check_Image_function_is_valid(pass_function_img_var))
        
        self.assertTrue(not check_Image_function_is_valid(fail_function_var))
        
        tester = validation_image_tester()
        
        self.assertTrue(check_Image_function_is_valid(tester.pass_function_self_img))
        
        self.assertTrue(check_Image_function_is_valid(tester.pass_function_self_img_var))
        
        self.assertTrue(not check_Image_function_is_valid(tester.fail_function_self_var))
        
        
    def test_csv_function_validation(self):
        
        from nanowire_flask.csv_tools import check_csv_function_is_valid
        
        
        def pass_function_csv_no_var(df):
            
            return {}
        
        def pass_function_csv_var(df, variables):
            
            return {}
        
        def fail_function_var(variables):
            
            return {}
        
        class validation_csv_tester(object):
            
            def pass_function_self_csv(self, df):
                
                return {}
            
            def pass_function_self_csv_var(self, df, variables):
                
                return {}
            
            def fail_function_self_var(self, variables):
                
                return {}
            
        self.assertTrue(check_csv_function_is_valid(pass_function_csv_no_var))            
        
        self.assertTrue(check_csv_function_is_valid(pass_function_csv_var))
        
        self.assertTrue(not check_csv_function_is_valid(fail_function_var))
        
        tester = validation_csv_tester()
        
        self.assertTrue(check_csv_function_is_valid(tester.pass_function_self_csv))
        
        self.assertTrue(check_csv_function_is_valid(tester.pass_function_self_csv_var))
        
        self.assertTrue(not check_csv_function_is_valid(tester.fail_function_self_var))
        
        
    def test_json_function_validation(self):
        
        from nanowire_flask.json_tools import check_json_function_is_valid
        
        
        def pass_function_json(inputJSON):
            
            return {}
        
        
        def fail_function_var(variables):
            
            return {}
        
        class validation_json_tester(object):
            
            def pass_function_self_json(self, inputJSON):
                
                return {}

            def pass_function_self_json_variables(self, inputJSON, variables):
                
                return {}
        
            def fail_function_self_var(self, variables):
                
                return {}
            
        self.assertTrue(check_json_function_is_valid(pass_function_json))            
        
        self.assertTrue(not check_json_function_is_valid(fail_function_var))
        
        tester = validation_json_tester()
        
        self.assertTrue(check_json_function_is_valid(tester.pass_function_self_json))
        
        self.assertTrue(not check_json_function_is_valid(tester.fail_function_self_var))

        self.assertTrue(check_json_function_is_valid(tester.pass_function_self_json_variables))


class test_file_server(unittest.TestCase):
    
    def test_file_cmd_line_send_file_direct_malformed_url(self):
        
        file_target = 'http://0.0.0.0:5006/model/predict'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"http://0.0.0.0:9999:/blah/blak\"}'"
            
        post_cmd += ' '
        post_cmd += file_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
       
        self.assertTrue('error' in out.keys())
        self.assertTrue(out['error'] == 'COULD NOT PULL FROM URL, PLEASE CHECK URL AND RETRY')
        
        
    def test_file_cmd_line_send_File_direct_fine(self):
        
        file_target = 'http://0.0.0.0:5006/model/predict'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"http://0.0.0.0:8001/test_text1.txt\"}'"
            
        post_cmd += ' '
        post_cmd += file_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
       
        self.assertTrue('result' in out.keys())
        self.assertTrue(out['result'] == 'Hello, This is a test!')
        
    def test_file_cmd_line_send_File_direct_malformed_json(self):
        
        file_target = 'http://0.0.0.0:5006/model/predict'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"http://0.0.0.0:8001/test_text1.txt\", \"threshold\":\"0.5}'"
            
        post_cmd += ' '
        post_cmd += file_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
       
        self.assertTrue('error' in out.keys())
        self.assertTrue(out['error'] == 'VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY')
        
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

#write the example csv
example_df.to_csv('example.csv', index=False)

#write the example xlsx file
example_df.to_excel('example.xlsx', index=False)

#generate an example json
example_dict = {'example':'of', 
                'a':[1,'2',True],
                'json':{'to':'be', 'loaded':'in'}
                }

with open("example.json", 'w') as f:
    f.write(json.dumps(example_dict))


print("KILLING THE SERVERS")

for p in range(7):
    os.system('fuser -k 500{0}/tcp'.format(p))

os.system('fuser -k 8001/tcp')

working_dir = os.getcwd()

if working_dir[-5:] == 'tests':

    os.system('python3 -m http.server 8001 &')

    os.chdir('../')

else:

    os.chdir('./tests')

    os.system('python3 -m http.server 8001 &')

    os.chdir('../')




#time.sleep(1)

print("STARTING TEXT SERVER")
#start the text server
run_text_cmd = 'python3 ./tests/text_server.py &'

result = os.system(run_text_cmd)

print("STARTING IMAGE SERVER")

run_img_cmd = 'python3 ./tests/image_server.py &'

result = os.system(run_img_cmd)

run_csv_cmd = 'python3 ./tests/csv_server.py &'

result = os.system(run_csv_cmd)

print("STARTING CSV SERVER")

run_JSON_cmd = 'python3 ./tests/json_server.py &'

result = os.system(run_JSON_cmd)

print("STARTING JSON SERVER")

run_file_cmd = 'python3 ./tests/file_server.py &'

result = os.system(run_file_cmd)

print("STARTING FILE SERVER")

#wait for the server to start
time.sleep(5)

#perform the unit tests
unittest.main()
#text_thread.exit()

print("KILLING THE SERVERS")

for p in range(7):
    os.system('fuser -k 500{0}/tcp'.format(p))
