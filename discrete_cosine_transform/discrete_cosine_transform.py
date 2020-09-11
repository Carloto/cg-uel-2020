from math import sqrt, cos, pi
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def apply_mask(img, m):
    """Aplica uma máscara"""
    mask_img = img.copy()
    for row in range(img.shape[0] - 2):
        for column in range(img.shape[1] - 2):
            mask_img[row+1, column+1] = m(img, row+1, column+1)

    return mask_img


def noise(img, n):
    noise_img = img.copy()
    for row in range(n//2, img.shape[0], n):
        noise_img[row, :] = 1

    return noise_img


def low_pass_filter(img, row, column):
    d_0 = 1

    return img[row, column] if img[row, column] <= d_0 else 0


def high_pass_filter(img, row, column):
    d_0 = 1

    return 0 if img[row, column] <= d_0 else img[row, column]


def discrete_cosine_transform(img):
    """Calcula a transformada discreta do cosseno em uma imagem n*n"""
    n = img.shape[0]
    dct_img = np.zeros((n, n))

    for row in range(n):
        for column in range(n):
            au = sqrt(1/n) if row == 0 else sqrt(2/n)
            av = sqrt(1/n) if column == 0 else sqrt(2/n)

            sum = 0
            for i in range(n):
                for j in range(n):
                    sum = sum + img[i][j] * cos((2 * i + 1) * row * pi / (
                        2 * n)) * cos((2 * j + 1) * column * pi / (2 * n))

            dct_img[row, column] = au*av*sum

    return dct_img


def inverse_discrete_cosine_transform(img):
    """Calcula a transformada discreta inversa do cosseno em uma imagem n*n"""
    n = img.shape[0]
    idct_img = np.zeros((n, n))

    for row in range(n):
        for column in range(n):
            au = sqrt(1/n) if row == 0 else sqrt(2/n)
            av = sqrt(1/n) if column == 0 else sqrt(2/n)

            sum = 0
            for i in range(n):
                for j in range(n):
                    sum = sum + \
                        img[i, j]*au*av*cos((2*i+1)*row*pi/(2*n)) * \
                        cos((2*j+1)*column*pi/(2*n))

            idct_img[row, column] = sum

    return idct_img


def main():
    img = cv.imread('../digital_ocean.png', cv.IMREAD_GRAYSCALE)

    img = cv.resize(img, (int(100), int(100)))

    noise_img = noise(img, 20)

    dct_img = discrete_cosine_transform(noise_img)
    cv.imwrite("dct_img.jpg", dct_img)

    l_p_img = apply_mask(dct_img, low_pass_filter)
    l_p_img = inverse_discrete_cosine_transform(l_p_img)
    cv.imwrite("low_pass_image.jpg", l_p_img)

    h_p_img = apply_mask(dct_img, high_pass_filter)
    h_p_img = inverse_discrete_cosine_transform(h_p_img)
    cv.imwrite("high_pass_image.jpg", h_p_img)

if __name__ == '__main__':
    main()
