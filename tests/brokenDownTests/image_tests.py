import json
import requests

from utils.file import lfile
from utils.server import ServerTest


class ImageServerTests(ServerTest):
    def setUp(self):
        self.start_server('image_server.py')


class image_server_test_case(ImageServerTests):

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

        out = self.send_json({"contentUrl": self.file_url('example_qr_code.bmp'),
                              "clean_text": 0})

        self.assertTrue('text' in out.keys())

        self.assertTrue('variables' in out.keys())

        self.assertTrue('shape' in out.keys())

        self.assertTrue(out['text'] == "Example image")


class test_image_server_test_case_cmd_line(ImageServerTests):

    def test_img_cmd_line_send_file_direct(self):
        out = self.send_file_curl('example_qr_code.png')

        self.assertTrue('text' in out.keys())
        self.assertTrue('variables' in out.keys())
        self.assertTrue(out['text'] == "Example image")

    def test_img_cmd_line_send_file_direct_malformed_json(self):
        out = self.send_json_curl(
            '{\"contentUrl\"::\"urlExample, \"threshold\":0.5}')
        self.assertTrue('error' in out.keys())
        self.assertTrue(
            out['error'] == 'VARIABLES JSON IS MALFORMED, PLEASE EXAMINE YOUR REQUEST AND RETRY')

    def test_img_cmd_line_send_file_direct_malformed_url(self):
        out = self.send_json_curl(
            '{\"contentUrl\":\"http://0.0.0.0:9999:/blah/blak\"}')

        self.assertTrue('error' in out.keys())
        self.assertTrue(
            out['error'] == 'COULD NOT PULL FROM URL, PLEASE CHECK URL AND RETRY')
