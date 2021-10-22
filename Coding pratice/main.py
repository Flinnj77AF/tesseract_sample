# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 07:12:49 2021

@author: flinn
"""

import cv2
import pytesseract as tes
try:
    from PIL import Image
except ImportError:
    import Image
    

tes.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():

    
    img_cv = cv2.imread(r'TechSmith-Blog-ExtractText.png')

    # By default OpenCV stores images in BGR format and sincce pytesseract assumes RGB format,
    # we need to convert from BGR to RGB format/mode:
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img_rgb, 5)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = (255-img)
    cv2.imshow('show', img)
    cv2.waitKey(1)
    txt = tes.image_to_string(img)
    print(repr(txt))
    input()
    
if __name__ == "__main__":
    main()