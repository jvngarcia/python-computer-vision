import numpy as np
import cv2

pic = cv2.imread('spiderman.jpeg', 0)


threshold_vlue = 80

(T_value, binary_threshold) = cv2.threshold(pic, threshold_vlue, 255, cv2.THRESH_BINARY)


cv2.imshow('Binary', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()