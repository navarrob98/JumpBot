import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from bot import Bot

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('BlueStacks')
# initialize the Vision class
vision_pilar1 = Vision('pilar1.png')
vision_pilar2 = Vision('pilar2.png')
vision_pilar3 = Vision('pilar3.png')
vision_pilar4 = Vision('pilar4.png')
vision_pilar5 = Vision('pilar5.png')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    points_1 = []
    points_2 = []
    points_3 = []
    points_4 = []        
    points_5 = []
    # display the processed image
    points_1 = vision_pilar1.find(screenshot, 0.5, 'rectangles')
    points_2 = vision_pilar2.find(screenshot, 0.5, 'rectangles')
    points_3 = vision_pilar3.find(screenshot, 0.5, 'rectangles')
    points_4 = vision_pilar4.find(screenshot, 0.5, 'rectangles')
    points_5 = vision_pilar5.find(screenshot, 0.5, 'rectangles')
    #clicker is bugged
    #if points_1 is not []:
        #clicker = Bot()
        #clicker.click()
        


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')