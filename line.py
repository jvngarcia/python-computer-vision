import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype =  'uint8') # Crea una imagen 500x500 fondo negro de int 8

cv2.line(pic, (350,350), (500, 350), (0,0,255))

cv2.imshow('Dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()