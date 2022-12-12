import cv2 

alahly = cv2.imread("Media/ALAHLY.jpg")

# TODO : CONVERT FROM BGR TO :
#1 GRAYSCALE
gray_Image = cv2.cvtColor(alahly, cv2.COLOR_BGR2GRAY)

#2 BINARY
(th,binary_image) = cv2.threshold(gray_Image, 127, 255, cv2.THRESH_BINARY)
print(th)

#3 RGB
rgb_image = cv2.cvtColor(alahly, cv2.COLOR_BGR2RGB)

#4 HSV
hsv_alahly = cv2.cvtColor(alahly, cv2.COLOR_BGR2HSV)

cv2.imshow("Orignal", alahly)
cv2.imshow("Gray", gray_Image)
cv2.imshow("Binary", binary_image)
cv2.imshow("RGB", rgb_image)
cv2.imshow("HSV", hsv_alahly)

cv2.waitKey()
cv2.destroyAllWindows()