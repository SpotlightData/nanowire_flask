import json
import requests

from utils.file import lfile
from utils.server import ServerTest


class CSVServerTest(ServerTest):
    def setUp(self):
        self.start_server('csv_server.py')


class csv_server_test_case(CSVServerTest):
    def test_from_file_csv(self):

        f = open(lfile('./example.csv'), 'rb')
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
        f = open(lfile('./example.xlsx'), 'rb')
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


class test_csv_server_cmd_line(CSVServerTest):

    def test_csv_cmd_line_sent_file_direct(self):
        out = self.send_file_curl('example.csv')
        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['shape'] == [2, 3])

    def test_xlsx_cmd_line_sent_file_direct(self):
        out = self.send_file_curl('example.xlsx')

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['shape'] == [2, 3])

    def test_xlsx_cmd_line_bad_file_url(self):

        out = self.send_json_curl(
            '{"contentUrl":"http://0.0.0.0:8029/example.csv", "ignore_col":"dates"}')

        self.assertTrue(
            out['error'] == "CANNOT CONNECT TO FILE URL, CHECK FILE URL AND TRY AGAIN")

    def test_xlsx_cmd_line_malformed_json(self):
        out = self.send_json_curl(
            '{"contentUrl"::"http://0.0.0.0:8001/example.csv", "ignore_col":"dates"}')
        self.assertTrue(
            out['error'] == "VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY")
