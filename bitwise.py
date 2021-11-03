import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), np.uint8)

rectangle = cv.rectangle(blank.copy(), (30, 20), (370, 370), (255, 255, 255), -1)

circle = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise AND --> intersection
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# bitwise OR --> union
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# bitwise XOR --> exclusive OR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# bitwise NOT --> inverse
bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)
