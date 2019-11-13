import time
import json
import threading
import requests
import os
import signal
import unittest
import tracemalloc

import pandas as pd
from pprint import pprint


from http.server import HTTPServer, SimpleHTTPRequestHandler
from utils.server import get_open_port, start_server, ServerTest
import functools


directory = os.path.realpath(__file__)


def local_file(name):
    return os.path.join(directory, './files', name)


class csv_server_test_case(ServerTest):
    def setUp(self):
        self.start_server('csv_server.py')

    def test_basic(self):
        a = ""
        # print(self.file_server_port)
        # print(self.file_server_url)


tracemalloc.start()
unittest.main()
# class csv_server_test_case(unittest.TestCase):

#     def test_from_file_csv(self):

#         text_target = 'http://0.0.0.0:5002/model/predict'

#         files = {'csv': ('./example.csv', open('./example.csv', 'rb'))}

#         r = requests.post(text_target + '?threshold=0.5', files=files)

#         out = r.json()

#         self.assertTrue('text' in out.keys())

#         self.assertTrue('variables' in out.keys())

#         self.assertTrue('shape' in out.keys())

#         self.assertTrue(out['shape'] == [2, 3])

#     def test_from_server_csv(self):

#         text_target = 'http://0.0.0.0:5002/model/predict'

#         csv_url = 'http://0.0.0.0:8001/example.csv'

#         d = json.dumps({"contentUrl": csv_url,
#                         "clean_text": 1})

#         heads = {"Content-Type": "application/json"}

#         r = requests.post(text_target, headers=heads, data=d)

#         out = r.json()

#         self.assertTrue('text' in out.keys())

#         self.assertTrue('variables' in out.keys())

#         self.assertTrue('shape' in out.keys())

#         self.assertTrue(out['shape'] == [2, 3])

#     def test_from_file_xlsx(self):

#         text_target = 'http://0.0.0.0:5002/model/predict'

#         files = {'xlsx': ('./example.xlsx', open('./example.xlsx', 'rb'))}

#         r = requests.post(text_target + '?threshold=0.5', files=files)

#         out = r.json()

#         self.assertTrue('text' in out.keys())

#         self.assertTrue('variables' in out.keys())

#         self.assertTrue('shape' in out.keys())

#         self.assertTrue(out['shape'] == [2, 3])

#     def test_from_server_xlsx(self):

#         text_target = 'http://0.0.0.0:5002/model/predict'

#         csv_url = 'http://0.0.0.0:8001/example.xlsx'

#         d = json.dumps({"contentUrl": csv_url,
#                         "clean_text": 1})

#         heads = {"Content-Type": "application/json"}

#         r = requests.post(text_target, headers=heads, data=d)

#         out = r.json()

#         self.assertTrue('text' in out.keys())

#         self.assertTrue('variables' in out.keys())

#         self.assertTrue(out['variables']['clean_text'] == 1)

#         self.assertTrue('shape' in out.keys())

#         self.assertTrue(out['shape'] == [2, 3])
