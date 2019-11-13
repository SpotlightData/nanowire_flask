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


directory = os.path.dirname(os.path.realpath(__file__))


def local_file(name):
    return os.path.join(directory, './files', name)


class csv_server_test_case(ServerTest):
    def setUp(self):
        self.start_server('csv_server.py')

    def test_from_file_csv(self):

        f = open(local_file('./example.csv'), 'rb')
        files = {
            'csv': ('./example.csv', f)}
        r = requests.post(self.url + '?threshold=0.5', files=files)
        f.close()

        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['shape'] == [2, 3])

    def test_from_server_csv(self):

        d = json.dumps({"contentUrl": self.file_url('example.csv'),
                        "clean_text": 1})

        heads = {"Content-Type": "application/json"}

        r = requests.post(self.url, headers=heads, data=d)

        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['shape'] == [2, 3])

    def test_from_file_xlsx(self):
        f = open(local_file('./example.xlsx'), 'rb')
        files = {
            'xlsx': ('./example.xlsx', f)}

        r = requests.post(self.url + '?threshold=0.5', files=files)
        f.close()
        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['shape'] == [2, 3])

    def test_from_server_xlsx(self):

        d = json.dumps({"contentUrl": self.file_url('example.xlsx'),
                        "clean_text": 1})

        heads = {"Content-Type": "application/json"}

        r = requests.post(self.url, headers=heads, data=d)

        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue(out['variables']['clean_text'] == 1)

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['shape'] == [2, 3])


class text_server_test_case(ServerTest):
    def setUp(self):
        self.start_server('text_server.py')

    def test_text_json_example(self):

        d = json.dumps({"text": "Example of text.",
                        "clean_text": 0,
                        "deactivate_entities": 0,
                        "deactivate_summary": 0})

        heads = {"Content-Type": "application/json"}

        r = requests.post(self.url, headers=heads, data=d)

        out = r.json()

        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example of text.")

    def test_text_file_example(self):

        text_target = 'http://0.0.0.0:5000/model/predict'
        f = open(local_file('test_text2.txt'), 'rb')
        files = {'doc': ('test_text2.txt', f)}
        r = requests.post(text_target + '?threshold=0.1', files=files)
        f.close()
        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('threshold' in out['variables'].keys())

        with open(local_file('test_text2.txt'), "r") as f:
            t = f.read()
            f.close()

        self.assertTrue(out['text'] == t)

    def test_text_from_server(self):

        d = json.dumps({"contentUrl": self.file_url('test_text3.txt'),
                        "clean_text": 0})

        heads = {"Content-Type": "application/json"}

        r = requests.post(self.url, headers=heads, data=d)

        out = r.json()
        print(out)

        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())

        with open(local_file('test_text3.txt'), "r") as f:
            t = f.read()
            f.close()

        self.assertTrue(out['text'] == t)


tracemalloc.start()
unittest.main()
