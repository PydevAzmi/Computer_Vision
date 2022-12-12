import cv2
from matplotlib import  pyplot as plt

# TODO:IMAGE READING
Orignal = cv2.imread("Media\PUBG.jpg")

# mode of image read
#1 GRAYSCALE
GRAYSCALE = cv2.imread("Media\PUBG.jpg", cv2.IMREAD_GRAYSCALE)

#2 COLOR
COLORED = cv2.imread("Media\PUBG.jpg", cv2.IMREAD_COLOR)

#3 REDUCED_COLOR_2
REDUCED_COLOR_4 = cv2.imread("Media\PUBG.jpg", cv2.IMREAD_REDUCED_COLOR_4) # _2

#4 REDUCED_GRAYSCALE_8
REDUCED_GRAYSCALE_8 = cv2.imread("Media\PUBG.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4)

#5 ANYCOLOR, UNCHANGED, ANYDEPTH
ANYDEPTH = cv2.imread("Media\PUBG.jpg", cv2.IMREAD_ANYDEPTH)
UNCHANGED = cv2.imread("Media\PUBG.jpg", cv2.IMREAD_UNCHANGED)

'''
cv2.imshow("ANYDEPTH", ANYDEPTH)
cv2.waitKey(5000)
cv2.destroyAllWindows()
'''

plt.subplot(2, 3, 1), plt.imshow(Orignal), plt.title("Orignal")
plt.subplot(2, 3, 2), plt.imshow(GRAYSCALE), plt.title("GRAYSCALE")
plt.subplot(2, 3, 3), plt.imshow(COLORED), plt.title("COLORED")
plt.subplot(2, 3, 4), plt.imshow(REDUCED_COLOR_4), plt.title("REDUCED_COLOR_4")
plt.subplot(2, 3, 5), plt.imshow(ANYDEPTH), plt.title("ANYDEPTH")
plt.subplot(2, 3, 6), plt.imshow(UNCHANGED), plt.title("UNCHANGED")

