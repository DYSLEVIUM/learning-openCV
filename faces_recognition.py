import numpy as np
import cv2 as cv
import os

people = []
dir = r"./train"

for i in os.listdir(dir):
    people.append(i)

haar_cascade = cv.CascadeClassifier("haarcascades_frontalface_default.xml")

# features = np.load("features.npy", allow_pickle=True)
# labels = np.load("labels.npy", allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread("./train/Ben Afflek/3.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Person", img)

# detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    # draw a rectangle around the face
    faces_roi = gray[y : y + h, x : x + w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with a confidence of {confidence}")

    cv.putText(
        img, str(people[label]), (20, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face", img)

cv.waitKey(0)
