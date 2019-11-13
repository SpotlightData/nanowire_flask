import json
import requests

from utils.file import lfile
from utils.server import ServerTest


class image_server_test_case(ServerTest):
    def setUp(self):
        self.start_server('image_server.py')

    def test_from_file_png(self):
        f = open(lfile('./example_qr_code.png'), 'rb')
        files = {'image': ('example_qr_code.png', f)
                 }

        r = requests.post(self.url + '?threshold=0.5', files=files)
        f.close()
        out = r.json()

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['text'] == "Example image")

    def test_from_file_jpg(self):

        with open(lfile('./example_qr_code.jpg'), 'rb') as f:
            files = {'image': ('./example_qr_code.jpg', f)}

            r = requests.post(self.url + '?threshold=0.5', files=files)

            out = r.json()

            self.assertTrue('text' in out.keys())

            self.assertTrue('variables' in out.keys())

            self.assertTrue('shape' in out.keys())

            self.assertTrue(out['text'] == "Example image")

    def test_from_file_jpeg(self):

        with open(lfile('./example_qr_code.jpeg'), 'rb') as f:
            files = {'image': ('./example_qr_code.jpeg', f)}

            r = requests.post(self.url + '?threshold=0.5', files=files)

            out = r.json()

            self.assertTrue('text' in out.keys())

            self.assertTrue('variables' in out.keys())

            self.assertTrue('shape' in out.keys())

            self.assertTrue(out['text'] == "Example image")

    def test_from_file_bmp(self):

        with open(lfile('./example_qr_code.bmp'), 'rb') as f:
            files = {'image': ('./example_qr_code.bmp', f)}

            r = requests.post(self.url + '?threshold=0.5', files=files)

            out = r.json()

            self.assertTrue('text' in out.keys())

            self.assertTrue('variables' in out.keys())

            self.assertTrue('shape' in out.keys())

            self.assertTrue(out['text'] == "Example image")

    def test_from_server_png(self):

        out = self.send_json({"contentUrl": self.file_url('example_qr_code.png'),
                              "clean_text": 0})

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['text'] == "Example image")

    def test_from_server_jpg(self):

        out = self.send_json({"contentUrl": self.file_url('example_qr_code.jpg'),
                              "clean_text": 0})

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['text'] == "Example image")

    def test_from_server_jpeg(self):
        out = self.send_json({"contentUrl": self.file_url('example_qr_code.jpeg'),
                              "clean_text": 0})

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['text'] == "Example image")

    def test_from_server_bmp(self):

        d = self.send_json({"contentUrl": self.file_url('example_qr_code.bmp'),
                            "clean_text": 0})

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['text'] == "Example image")
