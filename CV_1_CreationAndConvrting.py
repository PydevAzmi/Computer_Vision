import cv2
import numpy as np
import os

random_byte_array = bytearray(os.urandom(120000))
flat_number_array = np.array(random_byte_array)

# Make GRAYSCALE
grayImage = flat_number_array.reshape(300, 400)
cv2.imwrite("Media/Random_gray.png", grayImage)
# Make COLORED
colorImage = flat_number_array.reshape(100, 400, 3)
cv2.imwrite("Media/Random_color.png", colorImage)

random_color = cv2.imread("Media/Random_color.png")
random_gray = cv2.imread("Media/Random_gray.png")

cv2.imshow("# color", random_color)
cv2.imshow("# gray", random_gray)
cv2.waitKey(5000)
cv2.destroyAllWindows()