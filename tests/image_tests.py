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

    # def test_from_file_jpg(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     files = {'image': ('./example_qr_code.jpg',
    #                        open('./example_qr_code.jpg', 'rb'))}

    #     r = requests.post(text_target + '?threshold=0.5', files=files)

    #     out = r.json()

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")

    # def test_from_file_jpeg(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     files = {'image': ('./example_qr_code.jpeg',
    #                        open('./example_qr_code.jpeg', 'rb'))}

    #     r = requests.post(text_target + '?threshold=0.5', files=files)

    #     out = r.json()

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")

    # def test_from_file_bmp(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     files = {'image': ('./example_qr_code.bmp',
    #                        open('./example_qr_code.bmp', 'rb'))}

    #     r = requests.post(text_target + '?threshold=0.5', files=files)

    #     out = r.json()

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")

    # def test_from_server_png(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     image_url = 'http://0.0.0.0:8001/example_qr_code.png'

    #     d = json.dumps({"contentUrl": image_url,
    #                     "clean_text": 0})

    #     heads = {"Content-Type": "application/json"}

    #     r = requests.post(text_target, headers=heads, data=d)

    #     out = r.json()

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")

    # def test_from_server_jpg(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     image_url = 'http://0.0.0.0:8001/example_qr_code.jpg'

    #     d = json.dumps({"contentUrl": image_url,
    #                     "clean_text": 0})

    #     heads = {"Content-Type": "application/json"}

    #     r = requests.post(text_target, headers=heads, data=d)

    #     out = r.json()

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")

    # def test_from_server_jpeg(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     image_url = 'http://0.0.0.0:8001/example_qr_code.jpeg'

    #     d = json.dumps({"contentUrl": image_url,
    #                     "clean_text": 0})

    #     heads = {"Content-Type": "application/json"}

    #     r = requests.post(text_target, headers=heads, data=d)

    #     out = r.json()

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")

    # def test_from_server_bmp(self):

    #     text_target = 'http://0.0.0.0:5001/model/predict'

    #     image_url = 'http://0.0.0.0:8001/example_qr_code.bmp'

    #     d = json.dumps({"contentUrl": image_url,
    #                     "clean_text": 0})

    #     heads = {"Content-Type": "application/json"}

    #     r = requests.post(text_target, headers=heads, data=d)

    #     out = r.json()

    #     print("FROM SERVER BMP")
    #     print(out)
    #     print("+++++++++++++++++++++++++++++")

    #     self.assertTrue('text' in out.keys())

    #     self.assertTrue('variables' in out.keys())

    #     self.assertTrue('shape' in out.keys())

    #     self.assertTrue(out['text'] == "Example image")
