import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype =  'uint8') # Crea una imagen 500x500 fondo negro de int 8


font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(pic, 'Angel', (100, 100), font, 3, (255,255,255), 4, cv2.LINE_8)

cv2.imshow('Dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()