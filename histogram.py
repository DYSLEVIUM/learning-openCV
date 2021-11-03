import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("photos/lambo.jpg")
cv.imshow("Lambo", img)

# histogram helps to find the pixel distribution of the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
cv.imshow("Gray Histogram", gray_hist)

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
