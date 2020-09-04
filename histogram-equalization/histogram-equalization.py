import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def histogram(img):
    hist = np.zeros(256)
    for line in range(img.shape[0]):
        for pixel in img[line]:
            hist[pixel] += 1
    return hist


def normalize(hist, pixels):
    return hist/pixels


def cumulative(hist):
    cumulative_hist = np.zeros(256)
    cumulative_hist[0] = hist[0]
    for i in (range(hist.shape[0] - 1)):
        cumulative_hist[i+1] = cumulative_hist[i] + hist[i+1]
    return cumulative_hist

def equalization(img, hist):
    for line in range(img.shape[0]):
        for row in range(img.shape[1]):
            img[line, row] = (255*hist[img[line, row]]).astype(int)
    return img

def main():
    img = cv.imread('../color-converter/tokyo.jpg', cv.IMREAD_GRAYSCALE)
    cv.imwrite('gray.jpg', img)

    hist = histogram(img)
    plt.figure(1)
    plt.bar(range(256), hist)

    hist = normalize(hist, img.shape[0] * img.shape[1])
    plt.figure(2)
    plt.bar(range(256), hist)

    hist = cumulative(hist)
    plt.figure(3)
    plt.bar(range(256), hist)

    img = equalization(img, hist)
    cv.imwrite("equalized_img.jpg", img)

    plt.show()

if __name__ == '__main__':
    main()
