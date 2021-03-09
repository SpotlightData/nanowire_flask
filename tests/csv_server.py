#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:11:24 2019

@author: stuart
"""

# csv server

import time
import os
import nanowire_flask as nf
from nanowire_flask.csv_tools import mount_csv_function


def test_csv_function(df, variables):

    print('#########################')
    print(str(df))
    print('#########################')


    result = str(df['uuid'])

    out = {"text": result,
           "variables": variables,
           "shape": [len(df.columns), len(df)]}

    return out


print("FOUND VERSION", nf.__version__)

mount_csv_function(test_csv_function, port=5002)
