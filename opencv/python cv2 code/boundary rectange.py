import numpy as np
import cv2
img=cv2.imread("lena.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img=cv2.resize(img,(500,400))
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(len(contours))
for cnt in contours:
    if len(cnt)>1100:
        # print(cv2.contourArea(cnt))
        x,y,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

        cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()