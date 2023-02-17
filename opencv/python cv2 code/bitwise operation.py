import cv2
import matplotlib.pyplot as plt
img=cv2.imread("lena.png")
img2=cv2.imread("footbal.jpg")
img2=cv2.resize(img2,(640,480))
img=cv2.resize(img,(640,480))
bit_wise_or=cv2.bitwise_or(img,img2)
bit_wise_and=cv2.bitwise_and(img,img2)
bit_wise_xor=cv2.bitwise_xor(img,img2)
bit_wise_not=cv2.bitwise_not(img2)
cv2.imshow("original image lena",img)
cv2.imshow("original image footbal",img2)
cv2.imshow("bitwise or",bit_wise_or)
cv2.imshow("bitwise and",bit_wise_and)
cv2.imshow("bitwise xor",bit_wise_xor)
cv2.imshow("bitwise not",bit_wise_not)
a=[bit_wise_or,bit_wise_and,bit_wise_xor,bit_wise_not]
for i in range(len(a)):
    x=plt.subplot(2,2,i+1)
    plt.xticks([])
    plt.yticks([])
    x.imshow(a[i])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()