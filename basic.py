import cv2 as cv

img = cv.imread("photos/lambo.jpg")
cv.imshow("image", img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# blur
kernel_size = (7, 7)
blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# edge cascade (finds the edges that are present in an image)
canny = cv.Canny(img, 100, 200)
# cv.imshow("Canny", canny)

# dilate image using a structuring element(for this case is the canny edges)
dilated = cv.dilate(canny, kernel_size, iterations=1)
# cv.imshow("dilated", dilated)

# eroding
eroded = cv.erode(dilated, kernel_size, iterations=1)
# cv.imshow("eroded", eroded)

# resize
# resing-up
# resized = cv.resize(
#     img, (int(img.shape[1] * 2), int(img.shape[0] * 2)), interpolation=cv.INTER_LINEAR
# )

# slowest to res up
# resized = cv.resize(
#     img, (int(img.shape[1] * 2), int(img.shape[0] * 2)), interpolation=cv.INTER_CUBIC
# )

resized = cv.resize(
    img, (int(img.shape[1] // 2), int(img.shape[0] // 2)), interpolation=cv.INTER_AREA
)
# cv.imshow("resized", resized)

# cropping
cropped = img[100:400, 100:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
