from subprocess import PIPE
import subprocess
import socket
import os
import signal
import time

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
    process.stdout.close()


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

    def start_server(self, file):
        self.port = get_open_port()
        child_env = os.environ.copy()
        child_env['PORT'] = self.port
        self.server = start_server(file, str(self.port))
        self.url = 'http://0.0.0.0:{}/model/predict'.format(str(self.port))
        read_till(self.server, "Serving")
        # print("Running {} on {}".format(file, self.url))

    def tearDown(self):
        # print("Killing server {}".format(self.url))
        os.kill(self.server.pid, signal.SIGTERM)
        self.server.wait()
