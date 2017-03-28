import cv2
import numpy as np

im = cv2.imread('img/bears/1.jpg')

im = im / 112.5
im -= 1

print(im)