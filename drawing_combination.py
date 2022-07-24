import numpy as np
import cv2

color = ( 255, 0, 255 )

pic = np.zeros((500, 500, 3), dtype =  'uint8') # Crea una imagen 500x500 fondo negro de int 8


cv2.rectangle(pic, (0,0), (500, 150), color, 3, lineType = 8, shift = 0)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(pic, 'Angel', (100, 100), font, 3, color, 4, cv2.LINE_8)

cv2.line(pic, (133,138), (388, 133), color)

cv2.circle(pic, (250,250), 50, color)


cv2.imshow('Dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()