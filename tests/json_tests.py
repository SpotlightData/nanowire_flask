import json
import requests

from utils.file import lfile
from utils.server import ServerTest


class JSON_server_test_case(ServerTest):
    def setUp(self):
        self.start_server('json_server.py')

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
