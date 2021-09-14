# Chapter:7 Color Detection

import cv2
import numpy as np
import MyUtility 

cap = cv2.VideoCapture(0) # to read video
cap.set(3,640)
cap.set(4,480)


def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,340)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",152,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)


while True:
    success, img1 = cap.read()
    # cv2.imshow("Video",img2)

    img = cv2.imread("sample img/2.jpg")
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    imgresult = cv2.bitwise_and(img,img,mask=mask)
    

    stack = MyUtility.stackImages(0.5,([img,mask,imgresult]))
    cv2.imshow("Final",stack)
    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imghsv)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("Result",imgresult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break