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


#test the text processing tools with the requests library
class text_server_test_case(unittest.TestCase):
    
    def test_text_json_example(self):

        
        text_target = 'http://0.0.0.0:5000/model/predict'
        
        
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
    
#test the image processing tools with the requests library
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
        
#test the csv processing tools with the requests library
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
        
        
    def test_from_file_xlsx(self):
        
        text_target = 'http://0.0.0.0:5002/model/predict'
        
        files = {'xlsx': ('./example.xlsx', open('./example.xlsx', 'rb'))}
        
        r = requests.post(text_target + '?threshold=0.5', files=files)
        
        out = r.json()
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['shape'] == [2, 3])
        
    def test_from_server_xlsx(self):
        
        text_target = 'http://0.0.0.0:5002/model/predict'
        
        csv_url = 'http://0.0.0.0:8001/example.xlsx'
        
        d = json.dumps({"contentUrl":csv_url,
                "clean_text":1})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()
        
        self.assertTrue('text' in out.keys())
        
        self.assertTrue('variables' in out.keys())
        
        self.assertTrue(out['variables']['clean_text'] == 1)
        
        self.assertTrue('shape' in out.keys())
        
        self.assertTrue(out['shape'] == [2, 3])

        
        
#test the JSON processing tools with the requests library
class JSON_server_test_case(unittest.TestCase):
    
    def test_from_text_JSON(self):
        
        text_target = 'http://0.0.0.0:5003/model/predict'

        
        d = json.dumps({'example':'of', 
                'a':[1,2,3],
                'json':{'to':'be', 'loaded':'in'}
                })
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        
        self.assertTrue(out['example'] == 'of')
        self.assertTrue(out['json']['to'] == 'be')
        self.assertTrue(len(out['a']) == 3)
        
    def test_from_server_JSON(self):
        
        text_target = 'http://0.0.0.0:5003/model/predict'

        json_url = 'http://0.0.0.0:8001/example.json'
        
        d = json.dumps({"contentUrl":json_url,
                "clean_text":0})
        
        heads ={"Content-Type":"application/json"}
        
        r = requests.post(text_target, headers = heads, data=d)
        
        out = r.json()

        self.assertTrue(out['example'] == 'of')
        self.assertTrue(out['json']['to'] == 'be')
        self.assertTrue(len(out['a']) == 3)



#test the text processing tools with curl requests run in a shell
class test_text_server_test_case_cmd_line(unittest.TestCase):
    
    def test_text_cmd_line_send_txt_direct(self):

        
        text_target = 'http://0.0.0.0:5000/model/predict'
        
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"text\":\"Example of text.\", \"threshold\":0.5}'"
        
        post_cmd += ' '
        post_cmd += text_target
        
        out = os.popen(post_cmd).read()
        
        out = json.loads(out)
        
        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example of text.")
        
        

class test_image_server_test_case_cmd_line(unittest.TestCase):
    
    def test_img_cmd_line_send_file_direct(self):
        
        img_target = 'http://0.0.0.0:5001/model/predict'
        
        post_cmd = 'curl -F "image=@./example_qr_code.png" -XPOST ' + img_target
        
        out = os.popen(post_cmd).read()
 
        out = json.loads(out)
        
        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example image")
        
        
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
        
class test_json_server_cmd_line(unittest.TestCase):
    
    def test_json_send_from_server(self):
        
        json_target = 'http://0.0.0.0:5003/model/predict'
        
        json_source = 'http://0.0.0.0:8001/example.json'
        
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{\"contentUrl\":\"%s\"}' %s"%(json_source, json_target)

        out = os.popen(post_cmd).read()

        out = json.loads(out)
        
        self.assertTrue(out['example'] == 'of')
        self.assertTrue(out['json']['to'] == 'be')
        self.assertTrue(len(out['a']) == 3)

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
            

            def fail_function_self_var(self, variables):
                
                return {}
            
        self.assertTrue(check_json_function_is_valid(pass_function_json))            
        
        self.assertTrue(not check_json_function_is_valid(fail_function_var))
        
        tester = validation_json_tester()
        
        self.assertTrue(check_json_function_is_valid(tester.pass_function_self_json))
        
        self.assertTrue(not check_json_function_is_valid(tester.fail_function_self_var))

        
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

run_JSON_cmd = 'python3 ./json_server.py &'

result = os.system(run_JSON_cmd)

#wait for the server to start
time.sleep(5)

#perform the unit tests
unittest.main()
#text_thread.exit()




