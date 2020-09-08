import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def mean_filter(img):
    """Aplica o filtro da média"""
    mean_img = img.copy()
    for row in range(img.shape[0] - 2):
        for column in range(img.shape[1] - 2):
            for channel in range(3):
                mean_img[row+1, column+1,
                         channel] = mean(mean_img, row+1, column+1, channel)
    return mean_img


def mean(img, row, column, channel):
    """Calcula a média da região 3x3 de dado pixel"""
    mean = []
    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            mean.append(img[i, j, channel])

    return np.array(sum(mean)/9)


def main():
    img = cv.imread('../tokyo.jpg')

    mean_img = mean_filter(img)
    cv.imwrite("mean_filter.jpg", mean_img)


if __name__ == '__main__':
    main()
