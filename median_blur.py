import numpy as np
import cv2

pic = cv2.imread('spiderman.jpeg')

kernal = 3

median = cv2.medianBlur(pic, kernal)

cv2.imshow('Median', median)
cv2.waitKey(0)
cv2.destroyAllWindows()