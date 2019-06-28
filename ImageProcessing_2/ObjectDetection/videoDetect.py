import cv2
dataset = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
capture = cv2.VideoCapture('car_video/video_3.wmv')

while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame,None, fx=0.5, fy=0.5)
    if ret:
        faces = dataset.detectMultiScale(frame)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

        cv2.imshow('result', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")
cv2.destroyAllWindows()