# file = open('img_1.jpg','rb')
# data = file.read()
# print(data)
# file.close()

import cv2

img = cv2.imread('img_1.jpg')
# will print rgb color format of image
# print(img)
# print(img.shape)
font = cv2.FONT_HERSHEY_COMPLEX

while True:
    cv2.imshow('result',img)
    cv2.rectangle(img,(300,100),(450,230),(0,255,0),5)
    cv2.putText(img,'MS Dhoni',(300,100),font,1,(0,0,0),2)
    if cv2.waitKey(10) == 27:
        break