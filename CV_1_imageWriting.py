import cv2

# TODO: IMAGE WRITING

one_100_gray = cv2.imread("Media\PUBG.jpg",0)
cv2.imwrite("Media/New_PUBG.jpg", one_100_gray)
new_one_100 = cv2.imread("Media/New_PUBG.jpg")
cv2.imshow("#W", new_one_100)
cv2.waitKey()
cv2.destroyAllWindows()
