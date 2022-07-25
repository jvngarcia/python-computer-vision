import numpy as np
import cv2

pic = cv2.imread('spiderman.jpeg')

threshold_val1 = 50
threshold_val2 = 50

canny = cv2.Canny(pic, threshold_val1, threshold_val2)

cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()