import cv2
import numpy as np

dataset = cv2.CascadeClassifier('data.xml')

capture = cv2.VideoCapture(0)
facedata = []
while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),4)

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (50,50))
            if len(facedata) < 200:
                facedata.append(face)
                print(len(facedata))

        cv2.imshow('result',img)
        if cv2.waitKey(1) == 27 or len(facedata) >= 200:
            break
    else:
        print("Camera not working")

facedata = np.asarray(facedata)
np.save('user_2.npy',facedata)

cv2.destroyAllWindows()
capture.release()
