import numpy as np
import cv2

pic = cv2.imread('spiderman.jpeg')

matrix = (7,7)

blur = cv2.GaussianBlur(pic, matrix, 0)

cv2.imshow('Binary', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()