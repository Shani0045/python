import cv2
rect_kernal=cv2.getStructuringElement(cv2.MORPH_DILATE,(5,5))
rect_kernal=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
rect_kernal=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
rect_kernal=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
rect_kernal=cv2.getStructuringElement(cv2.MORPH_ERODE,(5,5))
rect_kernal=cv2.getStructuringElement(cv2.MORPH_OPEN,(5,5))
print(rect_kernal)
