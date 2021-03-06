import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from bot import Bot

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
#os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
vision_pilar1 = Vision('pilar1.png')
vision_pilar2 = Vision('pilar2.png')
vision_pilar3 = Vision('pilar3.png')
#vision_pilar4 = Vision('pilar4.png')
vision_pilar5 = Vision('pilar5.png')
vision_pilar6 = Vision('pilar6.png')
vision_pilar7 = Vision('pilar7.png')
#vision_pilar62 = Vision('pilar62.png')
vision_pilarPr = Vision('pilarpr.png')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    points_1 = []
    points_2 = []
    points_3 = []
    #points_4 = []        
    points_5 = []
    points_6 = []
    points_7 = []
    #points_62 = []
    points_pr =[]
    # display the processed image
    points_1 = vision_pilar1.find(screenshot, 0.45, 'rectangles')
    points_2 = vision_pilar2.find(screenshot, 0.6, 'rectangles')
    points_3 = vision_pilar3.find(screenshot, 0.6, 'rectangles')
    #points_4 = vision_pilar4.find(screenshot, 0.5)
    points_5 = vision_pilar5.find(screenshot, 0.6, 'rectangles')
    points_6 = vision_pilar6.find(screenshot, 0.6, 'rectangles')
    points_7 = vision_pilar7.find(screenshot, 0.6, 'rectangles')
    points_pr = vision_pilarPr.find(screenshot, 0.69, 'rectangles')
    #points_62 = vision_pilar62.find(screenshot,0.5, 'rectangles')
    if len(points_pr):
        print('pilar prohibido')
    elif len(points_1) or len(points_2) or len(points_3) or len(points_5) or len(points_6) or len(points_7):
        clicker = Bot()
        clicker.click()
    


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
