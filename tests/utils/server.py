import subprocess
import socket
import os
import signal

import unittest

directory = os.path.realpath(__file__)


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def run_child(commands, env):
    return subprocess.Popen(commands, env=env)


def start_server(name, port):
    file_path = os.path.join(directory, '..', name)
    child_env = os.environ.copy()
    child_env['PORT'] = port
    return run_child(['python3', file_path], child_env)


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start file server
        cls.file_server_port = get_open_port()
        cls.file_server_url = 'http://0.0.0.0:{}/'.format(
            str(cls.file_server_port))
        cls.file_server = run_child(
            ["python3",
             "-m",
             "http.server",
             "--directory",
             os.path.join(directory, '../files'),
             str(cls.file_server_port)], os.environ.copy())
        print("Running file server on {}".format(cls.file_server_url))

    @classmethod
    def tearDownClass(cls):
        print("Killing file server on {}".format(cls.file_server_url))
        os.kill(cls.file_server.pid, signal.SIGTERM)
        cls.file_server.wait()

    def start_server(self, file):
        self.port = get_open_port()
        child_env = os.environ.copy()
        child_env['PORT'] = self.port
        self.server = start_server(file, str(self.port))
        self.url = 'http://0.0.0.0:{}/model/predict'.format(str(self.port))
        print("Running {} on {}".format(file, self.url))

    def tearDown(self):
        print("Killing {}".format(self.url))
        os.kill(self.server.pid, signal.SIGTERM)
        self.server.wait()
