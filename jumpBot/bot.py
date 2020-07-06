from pyautogui import *
import pyautogui
import time
import win32api, win32con
#.72
#pyautogui.displayMousePosition()
#X:  150 Y:  826
class Bot:
    time.sleep(2)
    def __init__(self):
        pass
    #.68 known good
    def click(self):
        win32api.SetCursorPos((240,640))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.7)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
