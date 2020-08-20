import numpy as np
import cv2 as cv
import sys


def main():
    img = cv.imread(sys.argv[1])

    blue = img[..., 0]
    green = img[..., 1]
    red = img[..., 2]

    # RGB para CMYK

    cyan = 1 - (red/255)
    magenta = 1 - (green/255)
    yellow = 1 - (blue/255)

    black = np.minimum(np.minimum(cyan, magenta), yellow)

    with np.errstate(divide='ignore', invalid='ignore'):
        cyan = (cyan - black)/(1 - black)
        magenta = (magenta - black)/(1 - black)
        yellow = (yellow - black)/(1 - black)

    cyan[np.isnan(cyan)] = 0
    magenta[np.isnan(magenta)] = 0
    yellow[np.isnan(yellow)] = 0

    cv.imwrite('cmyk.png', cv.merge((cyan*255, magenta*255, yellow*255)))

    # RGB para HSI

    with np.errstate(divide='ignore', invalid='ignore'):
        theta = np.arccos(((1/2)*((red-green)+(red-blue))) /
                          (np.sqrt((((red-green)**2)+(red-blue)*(green-blue)))))
        theta[np.isnan(theta)] = 0

        hue = theta if (blue <= green).any() else 2*np.pi - theta
        hue = hue * 180 / np.pi

        saturation = 1 - 3 * \
            np.divide(np.minimum(np.minimum(red, blue), green),
                      blue + green + red)

        intensity = np.divide(blue + green + red, 3)

    cv.imwrite("hsi.png", cv.merge((hue,saturation,intensity)))

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
