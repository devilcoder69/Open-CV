# Chater: 2 Basic Functions
import cv2
import numpy as np

img = cv2.imread("sample img/1.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert your image into different color spaces
cv2.imshow("Gray Image",imgGray)

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # to blur the image
cv2.imshow("Blur Image",imgBlur)

imgCAnny = cv2.Canny(img,100,150) # Canny edge detector to find edges 
cv2.imshow("Canny Image",imgCAnny)

imgDialation = cv2.dilate(imgCAnny,kernel,iterations=1) # to increase thickness of canny images
cv2.imshow("Dilated Image",imgDialation)

imgErosion = cv2.erode(imgDialation,kernel,iterations=1) # to erode the image
cv2.imshow("Erosion Image",imgErosion) 

cv2.waitKey(0)

