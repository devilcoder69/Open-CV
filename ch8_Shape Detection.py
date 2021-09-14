# Chapter:8 Shape Detection
import cv2
import numpy as np
from numpy.lib.function_base import blackman
import MyUtility

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objCor == 3: 
                objectType = "Tri"
            elif objCor == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05:
                    objectType = "Sqaure"
                else:
                    objectType = "Rectangle"
            elif objCor == 5:
                objectType = "Pentagon"
            elif objCor == 6:
                objectType = "Hexagon"
            elif objCor == 7:
                objectType = "Heptagon"
            elif objCor == 8:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05:
                    objectType = "Octagon"
                else:
                    objectType = "Circles"
            elif objCor == 9:
                objectType = "Nonagon"
            elif objCor == 10:
                objectType = "Decagon"
            else:
                objectType = "None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(imgContour,objectType,(x+(w//2)-25,y+(h//2)-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),4)


img = cv2.imread('sample img/6.jpg')
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),2)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


imgblank = np.zeros((200,200),np.uint8)
stack = MyUtility.stackImages(0.4, ([img,imgGray,imgBlur],[imgCanny,imgContour,imgblank]))
cv2.imshow("Stackimg",stack)

# cv2.imshow("Original", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)

cv2.waitKey(0)