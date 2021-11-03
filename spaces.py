import cv2 as cv

img = cv.imread("photos/lambo.jpg")
cv.imshow("Lambo", img)

# bgr to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# bgr to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)