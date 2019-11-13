import json
import requests
import os
import unittest
import tracemalloc
from utils.server import ServerTest

# from csv_tests import csv_server_test_case
# from text_tests import text_server_test_case
from image_tests import image_server_test_case

tracemalloc.start()
unittest.main()
