import numpy as np
import cv2 as cv
import sys

def removeChannels(img, a, b):
    '''Remove two channels from the image.'''
    img[:,:,a] = 0
    img[:,:,b] = 0


def main():
    img = cv.imread(sys.argv[1]) # Image in BGR color format

    blue = img[...,0]
    green = img[...,1]
    red = img[...,2]

    # RGB para CMYK
    
    cyan = 1 - (red/255)
    magenta = 1 - (green/255)
    yellow = 1 - (blue/255)

    black = np.amin((cyan, magenta, yellow), axis=0)

    cyan = (cyan - black)/(1 - black)
    magenta = (magenta - black)/(1 - black)
    yellow = (yellow - black)/(1 - black)

    cv.imwrite('cmyk.png',cv.merge((cyan*255,magenta*255,yellow*255)))

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()