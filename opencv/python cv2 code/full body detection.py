import cv2
import imutils
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
img=cv2.imread("f:/varunjpg.jpg")
cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()