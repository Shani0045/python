import cv2
img=cv2.imread("lena.png",0)
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,1)
thresh1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,1)
cv2.imshow("output_gausian_c",thresh)
cv2.imshow("output_meanc",thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()