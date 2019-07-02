import cv2
import numpy as np
import os

current_dir = os.getcwd()
os.chdir(current_dir + '\\faces')
files = os.listdir()
faces = []
faceLength = [0]
users = {}

for i in range(len(files)):
    userName = files[i].split('.')[0]
    users[i] = userName

# print(users)

for file in files:
    face = np.load(file)
    face = face.reshape(face.shape[0], -1)
    faces.append(face)
    faceLength.append(len(face))

faces = np.vstack(faces)
labels = np.zeros((len(faces), 1))
partition = len(files)
# print(faceLength)
count = 0

slice_1 = 0
slice_2 = 0

for i in range(len(faceLength) - 1):
    slice_1 = faceLength[i]
    slice_2 = faceLength[i + 1]
    labels[slice_1:slice_2 + slice_1] = float(i)
# print(labels)


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

dataset = cv2.CascadeClassifier('../data.xml')
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread('../gallery27.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inputImageFaces = dataset.detectMultiScale(img)
for x, y, w, h in inputImageFaces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    face = gray[y:y + h, x:x + w]
    face = cv2.resize(face, (50, 50))

    label = knn(face.flatten(), faces)
    name = users[int(label)]
    # print(label)
    cv2.putText(img, name, (x, y), font, 1, (0, 0, 0), 2)

while True:
    cv2.imshow('result', img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

'''
capture = cv2.VideoCapture(0)

while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inputImageFaces = dataset.detectMultiScale(gray)
        for x,y,w,h in inputImageFaces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),4)

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (50,50))

            label = knn(face.flatten(), faces)
            name = users[int(label)]
            # print(label)
            cv2.putText(img,name,(x,y),font,1,(0,0,0),2)

        cv2.imshow('result', img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")

cv2.destroyAllWindows()
capture.release()
'''
