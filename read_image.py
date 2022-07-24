import numpy as np
import cv2

img = cv2.imread( 'spiderman.jpeg', -1 ) # Leer la imagen
img = cv2.imwrite( 'spiderman-tom.png', img ) # Cambiar el formato de imagen e incluso el nombre
cv2.imshow('Spiderman', img) # Mostrar la imagen asignadole un nombre
cv2.waitKey(0)
cv2.destroyAllWindows()