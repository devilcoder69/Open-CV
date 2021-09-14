# Chapter:1 Read Images Videos & Webcams

import cv2
# print("Package Imported")

# # for image
# img = cv2.imread("sample img/1.jpg") # to read an iamge
# cv2.imshow("Output", img)  # to display an image
# cv2.waitKey(0) # to hold the image until a key press

# # for videos
# cap = cv2.VideoCapture("sample vid/1.mp4") # to read video
# while True:
#     success, img2 = cap.read()
#     cv2.imshow("Video",img2)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# for webcam
cap = cv2.VideoCapture(0) # to read video
cap.set(3,640)
cap.set(4,480)

while True:
    success, img2 = cap.read()
    cv2.imshow("Video",img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
