# Chapter:8.2 Real time shape detection
import cv2
import numpy as np
import MyUtility

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty():
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,340)
cv2.createTrackbar("Threshold1","Parameters",10,255,empty)
cv2.createTrackbar("Threshold2","Parameters",22,255,empty)
cv2.createTrackbar("Area","Parameters",5000,100000,empty)

def getContours(img,imgContour):
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areamin = cv2.getTrackbarPos("Area","Parameters")
        if area > areamin:
            cv2.drawContours(imgContour, cnt, -1, (255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y),(x+w , y+h),(0,255,0),7)
            cv2.putText(imgContour, "Points: "+ str(len(approx)),(x + w + 20 , y + 20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
            cv2.putText(imgContour, "Area: "+ str(int(area)),(x + w + 20 , y + 45),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)



while True:
    success, img1 = cap.read()
    img = cv2.imread('sample img/6.jpg')
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7,7),5)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
    imgBlank = np.zeros((200,200),np.uint8)

    threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)

    kernel = np.ones((5,5))
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)

    getContours(imgDilation,imgContour)

    stack = MyUtility.stackImages(0.5,([img,imgBlur,imgGray],[imgCanny,imgDilation,imgContour]))

    cv2.imshow("Video",stack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
