import cv2
import numpy as np

face_1 = np.load('user_1.npy')
face_2 = np.load('user_2.npy')

face_1 = face_1.reshape(200,-1)
face_2 = face_2.reshape(200,-1)

faceData = np.concatenate([face_1,face_2])

username = {0:'Ravi',1:'Rishabh'}
labels = np.zeros((len(faceData),1))
labels[200:,:] = 1.0

def dist(x2,x1):
    return np.sqrt(sum((x2 - x1) ** 2))

def knn(x,train):
    n = train.shape[0]
    distance = []
    for i in range(n):
        distance.append(dist(x,train[i]))
    distance = np.asarray(distance)
    indexes = np.argsort(distance)
    sortedLabels = labels[indexes][:5]
    count = np.unique(sortedLabels, return_counts=True)
    return count[0][np.argmax(count[1])]

dataset = cv2.CascadeClassifier('data.xml')
capture = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX
while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inputImageFaces = dataset.detectMultiScale(gray)
        for x,y,w,h in inputImageFaces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),4)

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (50,50))

            label = knn(face.flatten(), faceData)
            name = username[int(label)]
            # print(label)
            cv2.putText(img,name,(x,y),font,1,(0,0,0),2)

        cv2.imshow('result', img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cv2.destroyAllWindows()
capture.release()
