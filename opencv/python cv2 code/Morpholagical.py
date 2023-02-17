import cv2
img=cv2.imread("lena.png")
dialte_kernal=cv2.getStructuringElement(cv2.MORPH_DILATE,(5,5))
dialate=cv2.morphologyEx(img,cv2.MORPH_DILATE,dialte_kernal)
cv2.imshow("output",dialate)
cv2.waitKey(0)
cv2.destroyAllWindows()