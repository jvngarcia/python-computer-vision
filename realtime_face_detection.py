import numpy as np
import cv2

#https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
scale_factor = 1.3


while 1:

    ret, pic = video_capture.read()

    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)

    for ( x, y , w, h ) in faces:

        center_x = (x + w) / 2

        cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'Face', ( int(center_x) , y + h), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    print('Number of faces found {}'.format(len(faces)))
    cv2.imshow('Faces', pic)
    k = cv2.waitKey(30) & 0xff
    if ( k == 2 ):
        break

cv2.destroyAllWindows()