import numpy as np
import pytesseract
import cv2
import pyautogui
import time
from PIL import ImageGrab

def imToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    while True:
        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox=(181, 633, 1956, 813))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(np.array(cap), cv2.COLOR_RGB2GRAY),
            lang='eng')
        # print(tesstr)
        texts = []

        for char in tesstr:
            if char == '\n':
                texts.append(' ')
                
            else:
                texts.append(char)
            
        time.sleep(5)    
        pyautogui.typewrite(''.join(texts), interval=0.1)
        

# Calling the function
imToString()
