#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:00:51 2019

@author: stuart
"""

# run an example image server


import numpy as np
import os
from pyzbar.pyzbar import decode

import nanowire_flask as nf

from nanowire_flask.image_tools import mount_Image_function


def test_image_function(img, variables):

    print("RECEVED IMAGE REQUEST")

    result = decode(img)

    out = {"text": result[0].data.decode(),
           "variables": variables,
           "shape": list(np.shape(img))}

    return out


print("FOUND VERSION", nf.__version__)

mount_Image_function(test_image_function, port=5001)
