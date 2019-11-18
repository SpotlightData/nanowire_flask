import json
import requests

from utils.file import lfile
from utils.server import ServerTest


class JSONServerTest(ServerTest):
    def setUp(self):
        self.start_server('json_server.py')


class JSON_server_test_case(JSONServerTest):
    def test_from_text_JSON(self):
        out = self.send_json({'example': 'of',
                              'a': [1, 2, 3],
                              'json': {'to': 'be', 'loaded': 'in'}
                              })

        self.assertTrue(out['inputJSON']['example'] == 'of')
        self.assertTrue(out['inputJSON']['json']['to'] == 'be')
        self.assertTrue(len(out['inputJSON']['a']) == 3)

    def test_from_server_JSON(self):
        out = self.send_json({"contentUrl": self.file_url('example.json'),
                              "clean_text": 0})

        self.assertTrue(out['inputJSON']['example'] == 'of')
        self.assertTrue(out['inputJSON']['json']['to'] == 'be')
        self.assertTrue(len(out['inputJSON']['a']) == 3)


class test_json_server_cmd_line(JSONServerTest):
    def json_file(self):
        return self.file_url('example.json')

    def test_json_send_from_server(self):
        out = self.send_json_curl(
            '{\"contentUrl\":\"%s\"}' % (self.json_file()))
        self.assertTrue(out['inputJSON']['a'] == [1, '2', True])
        self.assertTrue(out['inputJSON']['example'] == 'of')
        self.assertTrue(out['inputJSON']['json']['loaded'] == 'in')
        self.assertTrue(out['inputJSON']['json']['to'] == 'be')

    def test_json_bad_url(self):
        bad_url = "http://localhost:202020/test.json"
        out = self.send_json_curl(
            '{\"contentUrl\":\"%s\"}' % (bad_url))

        self.assertTrue(
            out['error'] == "CANNOT CONNECT TO FILE URL {0}, CHECK FILE URL AND TRY AGAIN".format(bad_url))

    def test_json_malformed_json(self):

        out = self.send_json_curl(
            '{\"contentUrl\"::\"%s\"}' % (self.json_file()))

        self.assertTrue(
            out['error'] == "VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY")

    def test_json_with_variables(self):
        out = self.send_json_curl(
            '{\"contentUrl\":\"%s\", \"customStops\":[\"horse\", \"course\"]' % (self.json_file()))
        self.assertTrue(
            out['error'] == "VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY")
