# Chapter:3 Resizing and Cropping
import cv2

img = cv2.imread("sample img/1.jpg")
print(img.shape)

imgResize = cv2.resize(img,(210,360))
print(imgResize.shape)
cv2.imshow("Image",img)
cv2.imshow("Image2",imgResize)

imgCropped = img[0:200,200:480]
# cv2.imshow("Image3",imgCropped)
cv2.waitKey(0)