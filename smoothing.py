import cv2 as cv
import numpy as np

img = cv.imread("photos/lambo.jpg")
cv.imshow("Lambo", img)

kernel = (5, 5)

# averaging (gets the average of the pixels in the kernel, and sets the middle pixel to that value)
blur = cv.blur(img, kernel)
cv.imshow("Averaging", blur)

# gaussian (similar to averaging, but it uses a gaussian distribution to calculate the average, i.e., it takes into account the pixels around the middle pixel (defines weight to each pixel in the kernel))
gaussian = cv.GaussianBlur(img, kernel, 0)  # 0 is the sigma value(standard deviation)
cv.imshow("Gaussian", gaussian)

# median (gets the median of the pixels in the kernel, and sets the middle pixel to that value)
median = cv.medianBlur(img, kernel[0])  # generally used to remove noise
cv.imshow("Median", median)

# bilateral (uses both the gaussian and the median filters, and combines them to get the best result)
bilateral = cv.bilateralFilter(
    img, kernel[0], 75, 75
)  # 75 is the sigma value for the gaussian filter, 75 is the sigma value for the median filter
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
