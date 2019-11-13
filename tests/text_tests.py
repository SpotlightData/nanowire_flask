import json
import requests

from utils.file import lfile
from utils.server import ServerTest


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

        f1 = open(lfile('test_text2.txt'), 'rb')
        files = {'doc': ('test_text2.txt', f1)}
        r = requests.post(self.url + '?threshold=0.1', files=files)
        f1.close()
        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('threshold' in out['variables'].keys())

        with open(lfile('test_text2.txt'), "r") as f:
            t = f.read()
            f.close()

        self.assertTrue(out['text'] == t)

    def test_text_from_server(self):

        d = json.dumps({"contentUrl": self.file_url('test_text3.txt'),
                        "clean_text": 0})

        heads = {"Content-Type": "application/json"}

        r = requests.post(self.url, headers=heads, data=d)

        out = r.json()

        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())

        with open(lfile('test_text3.txt'), "r") as f:
            t = f.read()
            f.close()

        self.assertTrue(out['text'] == t)
