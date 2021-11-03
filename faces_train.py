import os
import cv2 as cv
import numpy as np

people = []
dir = r"./train"

for i in os.listdir(dir):
    people.append(i)

haar_cascade = cv.CascadeClassifier("haarcascades_frontalface_default.xml")

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

            faces_rect = haar_cascade.detectMultiScale(
                img_array, scaleFactor=1.1, minNeighbors=5
            )

            for (x, y, w, h) in faces_rect:
                roi = img_array[y : y + h, x : x + w]
                features.append(roi)
                labels.append(label)


create_train()

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer
features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")

np.save("features.npy", features)
np.save("labels.npy", labels)

cv.waitKey(0)
