import cv2
img=cv2.imread("polygon.png")
img=cv2.resize(img,(640,480))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,190,255,cv2.THRESH_BINARY)
# thresh=cv2.Canny(thresh,100,150)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    a=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    cv2.drawContours(img,[a],0,(0,255,0),3)
    print(len(a))
    x,y=a[0][0]
    if len(a)==3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
    elif len(a)==4:
        cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
    elif len(a)== 6:
        cv2.putText(img,"Hexagonal", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),2)
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
