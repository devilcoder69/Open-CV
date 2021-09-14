# Chapter:6 Joining Images
import cv2
import numpy as np
import MyUtility

kernel = np.ones((5,5),np.uint8)
# function for join different scale and channel images 



# img = cv2.imread('sample img/1.jpg')
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img2 = cv2.GaussianBlur(img1,(7,7),0)
# img3 = cv2.Canny(img,100,150)
# img4 = cv2.dilate(img3,kernel,iterations=1)
# img5 = cv2.erode(img4,kernel,iterations=1)

cap = cv2.VideoCapture(0) # to read video
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    # cv2.imshow("Video",img)
    

    # img = cv2.imread('sample img/1.jpg')
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2 = cv2.GaussianBlur(img1,(7,7),10)
    img3 = cv2.Canny(img,100,150)
    img4 = cv2.dilate(img3,kernel,iterations=1)
    img5 = cv2.erode(img4,kernel,iterations=1)

    cv2.putText(img," Original ", (250,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(128,128,128),2)
    cv2.putText(img1," Gray ", (330,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(150,150,0),2)
    cv2.putText(img2," GrayBlur ", (225,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(150,150,0),2)
    cv2.putText(img3," Canny ", (290,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(150,150,0),2)
    cv2.putText(img4," Dilated ", (280,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(150,150,0),2)
    cv2.putText(img5," Eroded ", (275,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(150,150,0),2)

    imgStack = MyUtility.stackImages(0.5,([img,img1,img2],[img3,img4,img5]))
    cv2.imshow("Stack Image",imgStack)

    # Horizontal and Vertical stacking not work on different scaled or channel images 

    # imghor = np.hstack((img,img,img))
    # imgver = np.vstack((img,img))

    # cv2.imshow("Horizontal",imghor)
    # cv2.imshow("Vertical",imgver)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break