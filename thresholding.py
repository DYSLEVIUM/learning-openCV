import cv2 as cv

img = cv.imread("photos/lambo.jpg")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# simple thresholding
threshold, thres = cv.threshold(
    gray, 150, 255, cv.THRESH_BINARY
)  # 150 is the threshold value
cv.imshow("threshold", thres)

threshold, thres_inv = cv.threshold(
    gray, 150, 255, cv.THRESH_BINARY_INV
)  # 150 is the threshold value
cv.imshow("threshold inverse", thres_inv)

# adaptive thresholding
kernel = 11
# thres_adapt = cv.adaptiveThreshold(
#     gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, kernel, 2
# )
thres_adapt = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, kernel, 2
)
cv.imshow("adaptive threshold", thres_adapt)

cv.waitKey(0)
