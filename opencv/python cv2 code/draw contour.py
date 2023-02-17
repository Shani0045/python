import numpy as np
import cv2
img=cv2.imread("lena.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img=cv2.resize(img,(500,400))
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(len(contours))

for cnt in contours:
    rect=cv2.minAreaRect(cnt)
    box=cv2.boxPoints(rect)
    box=np.intc(box)
    if cv2.contourArea(cnt)>1200:
        im=cv2.drawContours(img,[box],0,(0,255,0),2)

        cv2.imshow("output",im)
cv2.waitKey(0)
cv2.destroyAllWindows()