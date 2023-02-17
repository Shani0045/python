import cv2
cap=cv2.VideoCapture("traffic.mp4")
while(True):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    a=cv2.Canny(gray,10,255)
    # _,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    d=cv2.getStructuringElement(cv2.MORPH_DILATE,(5,5))
    morph=cv2.morphologyEx(a,cv2.MORPH_DILATE,d)
    cnt,_=cv2.findContours(morph,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(frame,cnt,-1,(0,255,0),2)

    cv2.imshow("orignal",frame)
# cv2.imshow("gray",gray)
# cv2.imshow("thresh",thresh)
# cv2.imshow("morph",morph)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()