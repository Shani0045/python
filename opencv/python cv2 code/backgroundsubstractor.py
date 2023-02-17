import cv2

kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)
cap=cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)

    morph=cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    cv2.imshow("output",fgmask)
    cv2.imshow("morph",morph)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
print(cv2.__version__)