import numpy as np
import cv2

cap = cv2.VideoCapture('video.mp4')

fourcc = cv2.VideoWriter_fourcc( * 'XVID' )

fps = 30
frame_size = (720, 480)
out = cv2.VideoWriter( 'sample.avi', fourcc, fps, frame_size )

while( cap.isOpened() ):
    ret, frame = cap.read()
    cv2.imshow('Video', frame)

    if( cv2.waitKey(1) & 0xff == ord('q') ):
        break
out.release()
cap.release()
cv2.destroyAllWindows()