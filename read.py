import cv2 as cv

# reading an image
# img = cv.imread('photos/code.png')
# cv.imshow('Code', img)

# this tells the program to wait for a keypress
# cv.waitKey(0)

# reading a video (if VideoCapture is sent a number 0, it will open the first camera)
# capture = cv.VideoCapture("videos\Webinar for Charity.mp4")
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame)

    framerate = 24

    if cv.waitKey(framerate) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
