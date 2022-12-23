# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 07:12:49 2021

@author: flinn
"""

import cv2
import pytesseract as tes


def main():

    
    img_cv = cv2.imread(r'test_bed_Press_start_K.png')

    # By default OpenCV stores images in BGR format and sincce pytesseract assumes RGB format,
    # we need to convert from BGR to RGB format/mode:
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    #img = cv2.medianBlur(img_rgb, 5)
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #img = (255-img)
    cv2.imshow('show', img_rgb)
    cv2.waitKey(1)
    txt = tes.image_to_string(img_rgb)
    print(txt)
    input()
    
if __name__ == "__main__":
    main()