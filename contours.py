import cv2 as cv
import numpy as np

# contours are the boundary of an object, lines or curve that joins contiguous points (they are not as same as edges)

img = cv.imread("photos/lambo.jpg")
cv.imshow("Lambo", img)

blank = np.zeros(img.shape, np.uint8)
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny = cv.Canny(gray, 100, 200)
cv.imshow("Canny", canny)

# blur = cv.GaussianBlur(canny, (5, 5), 0)

ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Image", thresh)

# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow("Contours Drawn", blank)

print(f"{len(contours)} contour(s) found!")

cv.waitKey(0)
