import cv2
import numpy as np
img=cv2.imread("red-number-5.jpg")
img1=cv2.resize(img,(640,480))
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# blur=cv2.blur(gray,(7,7))
_,thresh=cv2.threshold(gray,230,255,0)
thresh=cv2.dilate(thresh,np.array((3,3),"float32"))
corners=cv2.goodFeaturesToTrack(thresh,25,0.1,10)
corners=np.intc(corners)
for i in corners:
    x,y=i.ravel()
    cv2.circle(img1,(x,y),10,255,-1)
cv2.imshow("output",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()