import cv2
import numpy as np

black = np.zeros((310, 410), dtype=np.uint8)
black[0:310,0:410] = 255
black = cv2.cvtColor(black,cv2.COLOR_GRAY2BGR)
alahly = cv2.imread("Media/ALAHLY.jpg",0)
alahly1 = cv2.imread("Media/ALAHLY.jpg")

ret, thresh = cv2.threshold(alahly,25,255,0)
contours, hiraracy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print(contours)
cv2.drawContours(black, contours, -1 ,(0, 0, 0) , 1)
cv2.imshow("BINARY",alahly)
cv2.imshow("org",alahly1)
cv2.imshow("black",black)
cv2.waitKey(5000)
cv2.destroyAllWindows()