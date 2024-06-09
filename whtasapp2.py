import pyautogui
import time

# print("Move your mouse to the desired location...")
# pyautogui.displayMousePosition()

def pixel_matches_color(x, y, expected_color, tolerance=10):
    actual_color = pyautogui.pixel(x, y)
    for i in range(3):
        if abs(actual_color[i] - expected_color[i]) > tolerance:
            return False
    return True

while not pixel_matches_color(1561, 945, (76, 194, 255)):
    time.sleep(1) 
print("Affan")
# Accepting Call
pyautogui.click(x=1561, y=945)
time.sleep(2)
# Muting
# pyautogui.click(x=975, y=905)
# time.sleep(2)
# Sharing Screen
pyautogui.click(x=854, y=911)
time.sleep(2)
# Share audio
pyautogui.click(x=819, y=619)
time.sleep(2)
# Share your window
pyautogui.click(x=518, y=146)
time.sleep(2)
# Sharing your display
pyautogui.click(x=520, y=188)
time.sleep(2)
# Display
pyautogui.click(x=918, y=383)
time.sleep(2)
# Okk
pyautogui.click(x=1300, y=876)
time.sleep(2)
# Wait for a period of time
print("over")
# For pressing cmd
pyautogui.click(x=1388, y=1049)
time.sleep(2)
# For pressing the cmd file
pyautogui.click(x=1277, y=921)
time.sleep(2)
# # Type something at a specific location
pyautogui.click(x=1416, y=466)
pyautogui.typewrite("python run.py")
time.sleep(1)
pyautogui.press('enter')  # Press Enter key
print("yuyyy")
# Opening Chrome
pyautogui.click(x=1441, y=1044)
time.sleep(2)
# # Type something at a specific location
pyautogui.click(x=1258, y=83)
pyautogui.typewrite("http://127.0.0.1:8000/")
time.sleep(1)
pyautogui.press('enter')  # Press Enter key
while not pixel_matches_color(1263, 874, (254, 218, 106)):
    time.sleep(1) 
# start
pyautogui.click(x=1263, y=874)
time.sleep(2)
# Click and drag from (1712, 15) to (655, 79)
# pyautogui.moveTo(1690, 23)
# pyautogui.dragTo(841, 91, duration=1.5)
# # Perform another mouse click at different location (x2, y2)
# pyautogui.click(x=300, y=400)

# # Wait for a period of time
# time.sleep(2)



# # Wait for a period of time
# time.sleep(2)

# # Move the mouse back to a specific location (optional)
# pyautogui.moveTo(x=100, y=100)

# You can continue with more actions as needed

