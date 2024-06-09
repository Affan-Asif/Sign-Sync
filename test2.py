import pyautogui
import time
from test import *

# print("Move your mouse to the desired location...")
# pyautogui.displayMousePosition()

def pixel_matches_color(x, y, expected_color, tolerance=10):
    actual_color = pyautogui.pixel(x, y)
    for i in range(3):
        if abs(actual_color[i] - expected_color[i]) > tolerance:
            return False
    return True

while not pixel_matches_color(1540, 940, (76, 194, 255)):
    time.sleep(1) 
print("Affan")
time.sleep(2)
# Accepting Call
pyautogui.click(x=1540, y=940)
time.sleep(2)


pyautogui.click(x=862, y=901)
time.sleep(2)

pyautogui.click(x=796, y=614)
time.sleep(2)

pyautogui.click(x=581, y=155)
time.sleep(2)

pyautogui.click(x=559, y=186)
time.sleep(2)

pyautogui.click(x=1075, y=370)
time.sleep(2)

pyautogui.click(x=1310, y=866)
time.sleep(2)
# sdfsjkgbkdjsgbskdjg
pyautogui.click(x=1332, y=1047)
time.sleep(2)

pyautogui.click(x=1053, y=927)
time.sleep(2)

pyautogui.click(x=1331, y=627)
pyautogui.typewrite("python run.py")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(x=1391, y=1046)
time.sleep(2)

pyautogui.click(x=1239, y=79)
pyautogui.typewrite("http://127.0.0.1:8000/")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
# afiubasufbisa

while not pixel_matches_color(1270, 872, (249, 214, 104)):
    time.sleep(1) 
pyautogui.click(x=1270, y=872)
time.sleep(2)
print("Affan")
while True:
# Accepting Call 
    print("Affan")
    time.sleep(2)
    pyautogui.click(x=1227, y=489)
    pyautogui.typewrite(transcribe_audio())
    time.sleep(2)
    pyautogui.click(x=1144, y=531)
    time.sleep(2)
    pyautogui.click(x=1669, y=461)
    time.sleep(2)

