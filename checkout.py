import cv2
import time

import cx_Oracle

import numpy as np
import pytesseract
from matplotlib import pyplot as plt
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img=Image.open('c1.png')

numplate=pytesseract.image_to_string(img)
print (numplate)
t = time.localtime()
current = time.strftime("%H:%M:%S", t)

conn=cx_Oracle.connect('HR/archin722@localhost/sac')
cur=conn.cursor()



cur.execute("update security set checkout='%s' where numplate='%s'" %(current,numplate))

cur.execute('commit')
cur.execute('select * from security')
for line in cur:
    print(line)
cur.close()
conn.close()









