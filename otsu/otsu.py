from math import sqrt
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def apply_otsu(img, T):
    """Aplica a a limiarização de otsu"""
    otsu_img = img.copy()
    for line in range(img.shape[0]):
        for column in range(img.shape[1]):
            otsu_img[line, column] = 0 if img[line, column] < T else 255
    return otsu_img


def histogram(img):
    """Calcula o histograma da imagem"""
    hist = np.zeros(256)
    for line in range(img.shape[0]):
        for pixel in img[line]:
            hist[pixel] += 1
    return hist


def probability(img, hist):
    """Calcula a função de probabilidade do histograma"""
    prob = np.zeros(256)
    n = img.shape[0] * img.shape[1]
    for q in range(256):
        prob[q] = hist[q]/n
    return prob


def otsu(prob):
    """Calcula o limiar T"""
    maximum = 0.0
    T = 1
    for t in range(1, 256):
        p1 = sum(prob[:t+1])
        p2 = 1 - p1
        m1 = 0
        for i in range(t+1):
            m1 += i * prob[i]
        m1 = m1 * (1/p1)
        m2 = 0
        for i in range(t+1, 256):
            m2 += i * prob[i]
        m2 = m2 * (1/p2)
        mg = 0
        for i in range(256):
            mg += i * prob[i]
        variance = p1 * (m1 - mg)**2 + p2 * (m2 - mg)**2
        if variance > maximum:
            maximum = variance
            T = t
    return T


def main():
    img = cv.imread('../lenna.png', cv.IMREAD_GRAYSCALE)

    cv.imwrite("gray_img.jpg", img)

    hist = histogram(img)
    hist_prob = probability(img, hist)

    T = otsu(hist_prob)
    otsu_img = apply_otsu(img, T)
    cv.imwrite("otsu_img.jpg", otsu_img)


if __name__ == '__main__':
    main()
