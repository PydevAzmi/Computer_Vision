import cv2

pubg = cv2.imread("Media/PUBG.jpg")

# TODO : SPLIT AND MERGE BGR IMAGES :
B, G, R = cv2.split(pubg)
merged_pubg=cv2.merge((B, G, R))

cv2.imshow("blue", B)
cv2.imshow("Green", G)
cv2.imshow("red", R)

cv2.imshow("merged_pubg", merged_pubg)

# TODO : SPLIT AND MERGE HSV IMAGES :
hsv_pubg = cv2.cvtColor(pubg, cv2.COLOR_BGR2HSV)
H=hsv_pubg[:,:,0]
S=hsv_pubg[:,:,1]
V=hsv_pubg[:,:,2]

cv2.imshow("hue", H)
cv2.imshow("saturation", S)
cv2.imshow("value", V)

cv2.waitKey()
cv2.destroyAllWindows()