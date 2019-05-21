#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:54:19 2019

@author: stuart
"""

#testing qr tools
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

img = qrcode.make("Example")

print("Image properties")
print(img)
print(type(img))

img.save('example_qr_code.png', 'PNG')


result = decode(Image.open('./example_qr_code.png'))

print("RESULT IS")
print(result[0].data.decode())
