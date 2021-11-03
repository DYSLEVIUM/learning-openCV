import cv2 as cv
import numpy as np

# gradients and edges are mathematically different but they can be used interchangeably programmatically

img = cv.imread("photos/lambo.jpg")
cv.imshow("Lambo", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))  # absolute value as images can't be negative
cv.imshow("Laplacian", lap)

# sobel
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow("Sobel X", sobelX)
cv.imshow("Sobel Y", sobelY)

combined = cv.bitwise_or(sobelX, sobelY)
cv.imshow("Combined Sobel", combined)

# canny is a multi-step process which uses sobel
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)
