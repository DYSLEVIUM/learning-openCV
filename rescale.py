import cv2 as cv

img = cv.imread("photos/code.png")

# works for images, videos, cameras, live videos, etc.
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width, height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


# another method of rescaling live video specifically
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


img_rescaled = rescaleFrame(img, 0.5)

cv.imshow("Image", img_rescaled)

cv.waitKey(0)


capture = cv.VideoCapture("videos\Webinar for Charity.mp4")

while True:
    isTrue, frame = capture.read()

    frame_rescaled = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_rescaled)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
