import cv2
import numpy as np

img = cv2.imread('Media\ALAHLY.jpg')

# Harris
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img )
corners= cv2.cornerHarris(gray_img , 2, 5, 0.07)
corners= cv2.dilate(corners, None)
th =  corners.max() * 0.01
img[corners > th]=[0, 0, 255]
cv2.imshow('Image with Borders', img)
cv2.waitKey()
cv2.destroyAllWindows()