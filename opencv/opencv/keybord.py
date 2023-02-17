import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    frame=cv2.resize(frame,(1350,720))
    cv2.rectangle(frame,(100,600),(1200,50),(0,255,0),5)
    cv2.putText(frame,"Digital Keybord",(440,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)
    cv2.line(frame,(100,120),(1200,120),(0,255,0),5)
    cv2.line(frame, (100, 150), (1200, 150), (0, 255, 0), 5)
    cv2.line(frame, (100, 120), (1200, 120), (0, 255, 0), 5)
    cv2.line(frame, (100, 120), (1200, 120), (0, 255, 0), 5)
    cv2.line(frame, (100, 120), (1200, 120), (0, 255, 0), 5)
    cv2.line(frame, (100, 120), (1200, 120), (0, 255, 0), 5)
    cv2.imshow("keyboard",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()