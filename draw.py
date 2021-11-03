import cv2 as cv
import numpy as np

# we can draw on an image also
# img = cv.imread('photos/code.jpg')

# blank image to draw on; here the shape is (width, height, channels)
blank = np.zeros((512, 512, 3), np.uint8)

# cv.imshow("Blank", blank)

# paint the image a certain color (b, g, r)
# blank[:] = (0, 0, 255)
# cv.imshow("Red", blank)

# blue square
# blank[200:300, 300:400] = (255, 0, 0)
# cv.imshow("Blue Square", blank)

# draw a rectangle
# cv.rectangle(blank, pt1=(100, 100), pt2=(300, 300), color=(0, 255, 0), thickness=2)

# -1 can be replaced with cv.FILLED
# cv.rectangle(blank, pt1=(100, 100), pt2=(300, 300), color=(0, 255, 0), thickness=-1)

# cv.rectangle(
#     blank,
#     (0, 0),
#     (blank.shape[0] // 2, blank.shape[1] // 2),
#     color=(0, 255, 0),
#     thickness=-1,
# )
# cv.imshow("Rectangle", blank)

# draw a circle
# cv.circle(blank, center=(200, 200), radius=100, color=(0, 255, 0), thickness=-1)
# cv.imshow("Circle", blank)

# draw a line
# cv.line(
#     blank,
#     pt1=(0, 0),
#     pt2=(blank.shape[1] // 2, blank.shape[0] // 2),
#     color=(0, 255, 0),
#     thickness=1,
# )
# cv.imshow("Line", blank)

# write text
cv.putText(
    blank,
    text="Pushpa",
    org=(100, 100),
    fontFace=cv.FONT_HERSHEY_TRIPLEX,
    fontScale=2,
    color=(0, 255, 0),
    thickness=2,
)
cv.imshow("Text", blank)

cv.waitKey(0)
