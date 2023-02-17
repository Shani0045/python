import cv2
import numpy as np
kernal=np.ones((5,5),"uint8")
img=cv2.imread("lena.png")
dialate=cv2.dilate(img,kernal,iterations=2)
erode=cv2.erode(img,kernal,iterations=2)

cv2.imshow("dialate",dialate)
cv2.imshow("erode",erode)
cv2.imshow("orignal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()