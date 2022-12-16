import cv2

alahly = cv2.imread("Media/ALAHLY.jpg")
# TODO: IMAGE RESIZING

# RESIZE TO HALF WITH FX, FY FATCTORS
half = cv2.resize(alahly, (0, 0), fx = 0.5, fy = 0.5)

# DEFAULT INTERPOLATION > LINEAR
bigger = cv2.resize(alahly, (720, 720))

# CHANGE  INTERPOLATION > NEAREST
stretch_near = cv2.resize(alahly, (720, 720),interpolation = cv2.INTER_NEAREST)

cv2.imshow("image", alahly)
cv2.imshow("half", half)
cv2.imshow("big", bigger)
cv2.imshow("stretch", stretch_near)

cv2.waitKey()
cv2.destroyAllWindows()