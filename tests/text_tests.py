import json
import requests

from utils.file import lfile
from utils.server import ServerTest


class TextServerTest(ServerTest):
    def setUp(self):
        self.start_server('text_server.py')


class text_server_test_case(TextServerTest):
    def test_text_json_example(self):

        out = self.send_json({"text": "Example of text.",
                              "clean_text": 0,
                              "deactivate_entities": 0,
                              "deactivate_summary": 0})

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

        out = self.send_json({"contentUrl": self.file_url('test_text3.txt'),
                              "clean_text": 0})

        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())

        with open(lfile('test_text3.txt'), "r") as f:
            t = f.read()
            f.close()

        self.assertTrue(out['text'] == t)


class test_text_server_test_case_cmd_line(TextServerTest):

    def test_text_cmd_line_send_txt_direct(self):
        out = self.send_json_curl(
            '{\"text\":\"Example of text.\", \"threshold\":0.5}')
        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example of text.")

    def test_text_cmd_line_malformed_cmd(self):
        out = self.send_json_curl(
            '{\"text\"::\"Example of text.\", \"threshold\":0.5}')

        self.assertTrue(
            out['error'] == 'VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY')

    def test_text_cmd_line_malformed_server_address(self):
        out = self.send_json_curl('{"contentUrl": "%s", "threshold": 0.5}' %
                                  ('http://localhost:2020203/test_text.txt'))

        self.assertTrue(
            out['error'] == "CANNOT CONNECT TO FILE URL, CHECK FILE URL AND TRY AGAIN")
