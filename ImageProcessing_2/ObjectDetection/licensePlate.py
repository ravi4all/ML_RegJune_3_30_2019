import cv2

img = cv2.imread('images/car_4.jpg')
dataset = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
plates = dataset.detectMultiScale(img,1.4)

# print(plates)

for x,y,w,h in plates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 5)

while True:

    cv2.imshow('result',img)
    if cv2.waitKey(10) == 27:
        break

cv2.imwrite('result_3.jpg',img)