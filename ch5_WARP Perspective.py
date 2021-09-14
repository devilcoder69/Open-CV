# Chapter:5 WARP Perspective
import cv2
import numpy as np



img = cv2.imread("sample img/3.jpg")
# img1 = cv2.resize(img,(550,450))
# cv2.imwrite('3.jpg',img1)

width,height = 250,350
pts1 = np.float32([[445,138],[543,226],[326,305],[422,395]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

# for x in range (0,4):
#     cv2.circle(img,(pts1[x][0],pts1[x][1]),15,(0,255,0),cv2.FILLED)

cv2.imshow("Image",img)
cv2.imshow("output",imgoutput)
cv2.waitKey(0)