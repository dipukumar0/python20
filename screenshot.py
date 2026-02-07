import time
import pyautogui

def screenshot():
    time.sleep(5)
    img = pyautogui.screenshot('text.png')
    img.show()


    screenshot()