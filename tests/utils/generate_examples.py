import time
import json
import threading
import requests
import os
import unittest
import qrcode

directory = os.path.realpath(__file__)


def epath(file):
    return os.path.join(directory, '../files/', file)


def generate_examples():
    # generate pngs, jpgs and bmps of qr codes to test the image server
    img = qrcode.make("Example image")

    img.save(epath('example_qr_code.png'))
    img.save(epath('example_qr_code.jpg'))
    img.save(epath('example_qr_code.jpeg'))
    img.save(epath('example_qr_code.bmp'))

    # generate the csvs for testing the csv server
    df_dict = {'uuid': ['t-001', 't-002', 't-003'],
               'texts': ['example', 'text', 'No3']}

    example_df = pd.DataFrame(df_dict)

    # write the example csv
    example_df.to_csv(epath('example.csv'), index=False)

    # write the example xlsx file
    example_df.to_excel(epath('example.xlsx'), index=False)

    # generate an example json
    example_dict = {'example': 'of',
                    'a': [1, '2', True],
                    'json': {'to': 'be', 'loaded': 'in'}
                    }

    with open(epath("example.json"), 'w') as f:
        f.write(json.dumps(example_dict))

    with open(epath("test_text1.txt"), 'w') as f:
        f.write(json.dumps(example_dict))
