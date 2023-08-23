import cv2 
img = cv2.imread("poster.jpg")
rocket = img[120:360, 400:500]
img[0:240, 500:600] = rocket
cv2.putText(img, "this is a rocket", (20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color = (255,255,255))
cv2.imshow("open1", rocket)
cv2.imshow("open", img)
cv2.waitKey(5000)
print(img)