from __future__ import print_function
import barcode
from barcode.writer import ImageWriter
from barcode import generate


import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

print(barcode.PROVIDED_BARCODES)
str1 = '916708280603'
EAN = barcode.get_barcode_class('ean13')
ean = EAN(str1)
fullname = ean.save('ean13_barcode')
ean = EAN(str1, writer=ImageWriter())

f = open('barcode3.svg', 'wb')
ean.write(f)

name = generate('EAN13', str1, output='barcode3_svg')
generate('EAN13', str1, writer=ImageWriter(), output='barcode')


