import pyautogui
import time

# Get the current position of the mouse cursor
while True:
    x, y = pyautogui.position()
    print(x,y)
    time.sleep(0.3)

# Get the RGB value of the pixel at the current position of the mouse cursor
#pixel_color = pyautogui.pixel(x, y)

# Print the RGB value of the pixel
#print(pixel_color)
