import numpy as np
import cv2

black_img = np.zeros((300, 400, 3), np.uint8)

# Drawing the triangle with the help of lines
cv2.line(black_img, (100, 200), (50, 50), (255, 255, 0), 2)
cv2.line(black_img, (50, 50), (300, 100), (255, 255, 0), 2)
cv2.line(black_img, (100, 200), (300, 100), (255, 255, 0), 2)

centroid = ((100 + 50 + 300) // 3, (200 + 50 + 100) // 3)

cv2.circle(black_img, centroid, 3, (255, 255, 0))

cv2.imshow("image", black_img)
cv2.waitKey()
cv2.destroyAllWindows()