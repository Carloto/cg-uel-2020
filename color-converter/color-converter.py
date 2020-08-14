import numpy as np
import cv2 as cv
import sys

def removeChannels(img, a, b):
    '''Remove two channels from the image.'''
    height, width, depth = img.shape
    img[0:height, 0:width, a] = 0
    img[0:height, 0:width, b] = 0

img = cv.imread(sys.argv[1]) # Image in BGR color format
blue = img.copy()
removeChannels(blue, 1, 2)
cv.imshow('blue',blue)
cv.waitKey(0)
cv.destroyAllWindows()