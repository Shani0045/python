import cv2
import time
img=cv2.imread("lena.png",1)
time=time.strftime("%H:%M:%S")
a=cv2.putText(img,"lena image",(100,500),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),3)
b=cv2.putText(a,time,(150,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
c=cv2.rectangle(b,(90,400),(400,50),(255,0,0),3)
cv2.imshow("gray scale",c)
cv2.waitKey(0)
cv2.destroyAllWindows()