import cv2
import matplotlib.pyplot as plt
img=cv2.imread("lena.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
_,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,thresh=cv2.threshold(img,127,255,cv2.THRESH_MASK)
_,thresh=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,thresh=cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)
_,thresh=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(thresh)
plt.xticks([]),plt.yticks([])
plt.show()
