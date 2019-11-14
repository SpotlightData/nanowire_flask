from subprocess import PIPE
import subprocess
import socket
import json
import requests
import os
import signal
import time

from utils.file import lfile
import unittest

directory = os.path.dirname(os.path.realpath(__file__))


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def run_child(commands, env):
    return subprocess.Popen(commands, env=env, stdout=PIPE, bufsize=64)


def start_server(name, port):
    file_path = os.path.join(directory, '..', name)
    child_env = os.environ.copy()
    child_env['PORT'] = port
    return run_child(['python3', '-u', file_path], child_env)


def read_till(process, message):
    for line in iter(process.stdout.readline, b''):
        if message in line.decode('utf-8'):
            break
        else:
            continue


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start file server
        cls.file_server_port = get_open_port()
        cls.file_server_url = 'http://0.0.0.0:{}'.format(
            str(cls.file_server_port))
        cls.file_server = run_child(
            ["python3",
             "-u",
             "-m",
             "http.server",
             "--directory",
             os.path.join(directory, '../files'),
             str(cls.file_server_port)], os.environ.copy())
        read_till(cls.file_server, "Serving HTTP")
        # print("Running file server on {}".format(cls.file_server_url))

    @classmethod
    def tearDownClass(cls):
        # print("Killing file server on {}".format(cls.file_server_url))
        os.kill(cls.file_server.pid, signal.SIGTERM)
        cls.file_server.wait()
        cls.file_server.stdout.close()

    def file_url(self, file):
        return self.file_server_url + '/' + file

    def start_server(self, file):
        self.port = get_open_port()
        child_env = os.environ.copy()
        child_env['PORT'] = self.port
        self.server = start_server(file, str(self.port))
        self.url = 'http://0.0.0.0:{}/model/predict'.format(str(self.port))
        read_till(self.server, "Serving")
        # print("Running {} on {}".format(file, self.url))

    def setUp(self):
        raise("Please define setUp method")

    def tearDown(self):
        # print("Killing server {}".format(self.url))
        os.kill(self.server.pid, signal.SIGTERM)
        self.server.wait()
        self.server.stdout.close()

    def send_json(self, data):
        d = json.dumps(data)
        heads = {"Content-Type": "application/json"}
        r = requests.post(self.url, headers=heads, data=d)
        return r.json()

    def send_json_curl(self, json_str):
        post_cmd = "curl -X POST -H \"Content-Type:application/json\" -d '{}' {}".format(
            json_str, self.url)
        proc = os.popen(post_cmd)
        out = json.loads(proc.read())
        proc.close()
        return out

    def send_file_curl(self, file_name):
        post_cmd = 'curl -F "image=@{}" -XPOST {}'.format(
            lfile(file_name), self.url)
        proc = os.popen(post_cmd)
        out = json.loads(proc.read())
        proc.close()
        return out
