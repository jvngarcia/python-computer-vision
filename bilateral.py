import numpy as np
import cv2

pic = cv2.imread('spiderman.jpeg')

dimpixel = 7
color = 100
space = 100

filter = cv2.bilateralFilter(pic, dimpixel, color, space)


cv2.imshow('Filter', filter)
cv2.waitKey(0)
cv2.destroyAllWindows()