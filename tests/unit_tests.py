import json
import requests
import os
import unittest
import tracemalloc
from utils.server import ServerTest

from text_tests import text_server_test_case, test_text_server_test_case_cmd_line
from image_tests import test_image_server_test_case_cmd_line, image_server_test_case
from csv_tests import csv_server_test_case, test_csv_server_cmd_line
from json_tests import JSON_server_test_case, test_json_server_cmd_line

tracemalloc.start()
unittest.main()
