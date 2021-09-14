# Chapter:9 Face Detection
import cv2

cap = cv2.VideoCapture(0) # to read video
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    # cv2.imshow("Video",img2)
    facecascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
    # img = cv2.imread('sample img/7.jpg')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
