import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def apply_mask(img, m):
    """Aplica uma máscara"""
    mask_img = img.copy()
    for row in range(img.shape[0] - 2):
        for column in range(img.shape[1] - 2):
            for channel in range(3):
                mask_img[row+1, column+1,
                         channel] = m(img, row+1, column+1, channel)
    return mask_img


def horizontal_sobel(img, row, column, channel):
    """Aplica o filtro sobel na região 3x3 de dado pixel"""
    h_sobel = []
    h_sobel.append(img[row, column, channel]*0)
    h_sobel.append(img[row, column+1, channel]*0)
    h_sobel.append(img[row, column-1, channel]*0)
    h_sobel.append(img[row-1, column, channel]*-2)
    h_sobel.append(img[row+1, column, channel]*2)
    h_sobel.append(img[row-1, column-1, channel]*-1)
    h_sobel.append(img[row-1, column+1, channel]*-1)
    h_sobel.append(img[row+1, column-1, channel])
    h_sobel.append(img[row+1, column+1, channel])

    return np.array(sum(h_sobel)/9)

def vertical_sobel(img, row, column, channel):
    """Aplica o filtro sobel na região 3x3 de dado pixel"""
    v_sobel = []
    v_sobel.append(img[row, column, channel]*0)
    v_sobel.append(img[row, column+1, channel]*2)
    v_sobel.append(img[row, column-1, channel]*-2)
    v_sobel.append(img[row-1, column, channel]*0)
    v_sobel.append(img[row+1, column, channel]*0)
    v_sobel.append(img[row-1, column-1, channel]*-1)
    v_sobel.append(img[row-1, column+1, channel]*1)
    v_sobel.append(img[row+1, column-1, channel]*-1)
    v_sobel.append(img[row+1, column+1, channel]*1)

    return np.array(sum(v_sobel)/9)

def laplace(img, row, column, channel):
    """Aplica o filtro laplaciano na região 3x3 de dado pixel"""
    laplace = []
    laplace.append(img[row, column, channel]*4)
    laplace.append(img[row, column+1, channel]*-1)
    laplace.append(img[row, column-1, channel]*-1)
    laplace.append(img[row-1, column, channel]*-1)
    laplace.append(img[row+1, column, channel]*-1)
    laplace.append(img[row-1, column-1, channel]*0)
    laplace.append(img[row-1, column+1, channel]*0)
    laplace.append(img[row+1, column-1, channel]*0)
    laplace.append(img[row+1, column+1, channel]*0)

    return np.array(sum(laplace)/9)


def main():
    img = cv.imread('../animal.jpg')

    h_sobel_img = apply_mask(img, horizontal_sobel)
    cv.imwrite("horizontal_sobel.jpg", h_sobel_img)

    v_sobel_img = apply_mask(img, vertical_sobel)
    cv.imwrite("vertical_sobel.jpg", v_sobel_img)

    cv.imwrite("sobel.jpg", v_sobel_img + h_sobel_img)
     
    laplace_img = apply_mask(img, laplace)
    cv.imwrite("laplace.jpg", laplace_img)



if __name__ == '__main__':
    main()
