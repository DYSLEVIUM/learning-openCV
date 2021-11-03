import cv2 as cv
import numpy as np

img = cv.imread("photos/lambo.jpg")
cv.imshow("Lambo", img)

# -x --> left
# -y --> up
# x --> right
# y --> down

# translation
def translate(image, x, y):
    # translate matrix looks like [[1, 0, x], [0, 1, y], [0, 0, 1]] -> this is a affine transformation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])

    dimensions = (image.shape[1], image.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

# rotation
def rotate(image, angle, center=None, scale=1.0):
    # rotate matrix looks like [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]] -> this is a affine transformation matrix
    (height, width) = image.shape[:2]

    # if no center is given, use the center of the image
    if center is None:
        center = (width // 2, height // 2)

    angle = np.radians(angle)

    # rotation matrix looks like [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]] -> this is a affine transformation matrix

    # rotMat = cv.getRotationMatrix2D(center, angle, scale)

    x0, y0 = ((width - 1) / 2.0, (height - 1) / 2.0)  # center of the image

    rotMat = np.float64(
        [
            [
                np.cos(angle),
                -np.sin(angle),
                x0 * (1 - np.cos(angle)) + y0 * np.sin(angle),
            ],
            [
                np.sin(angle),
                np.cos(angle),
                y0 * (1 - np.cos(angle)) - x0 * np.sin(angle),
            ],
        ]
    )

    return cv.warpAffine(image, rotMat, (width, height))


rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# resizing
def resize(image, scaled_width=None, scaled_height=None, inter=cv.INTER_CUBIC):
    dimensions = None
    (height, width) = image.shape[:2]

    if scaled_width is None and scaled_height is None:
        return image

    if scaled_width is None:
        ratio = scaled_height / float(height)
        dimensions = (int(width * ratio), scaled_height)

    elif scaled_height is None:
        ratio = scaled_width / float(width)
        dimensions = (scaled_width, int(height * ratio))
    else:
        dimensions = (scaled_width, scaled_height)

    return cv.resize(image, dimensions, interpolation=inter)


resized = resize(img, scaled_width=1500, scaled_height=100)
cv.imshow("Resized", resized)

# flip
# 1 --> horizontal, 0 --> vertical, -1 --> both
flip = cv.flip(img, 1)
cv.imshow("Flipped", flip)

# crop
cropped = img[100:400, 100:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
