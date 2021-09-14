# Chapter:4 Shapes and Texts
import cv2
import numpy as np

# img1 = np.ones((512,512))
img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[200:300,100:300] = 255,0,0

cv2.line(img,(50,50),(450,450),(0,255,0)) # (name,(start point),(end point),(color),(thickness))
# cv2.line(img,(50,50),(img.shape[0],img.shape[0]),(0,255,0),2) # for start to end of img

cv2.rectangle(img,(50,50),(350,350),(0,0,255),2) # (name,(start point),(end point),(color),(thickness))
# cv2.rectangle(img,(50,50),(350,350),(0,0,255),cv2.FILLED) 

cv2.circle(img,(350,350),70,(255,255,0),3) # (name,(center),(radius),(color),(thickness))

##########################
# TEXT

cv2.putText(img," DEVIL ", (150,40),cv2.FONT_HERSHEY_COMPLEX,1.5,(150,150,0),1) # (name,"TEXT",(location),font,size,color,thickness)

cv2.imshow("image",img)

cv2.waitKey(0)