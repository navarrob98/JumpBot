from pyautogui import *
import pyautogui
import time
import win32api, win32con

#pyautogui.displayMousePosition()
#X:  150 Y:  826
class Bot:
    time.sleep(2)
    def __init__(self):
        pass

    def click(self):
        win32api.SetCursorPos((240,640))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.68)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
