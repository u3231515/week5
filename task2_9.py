# task2_9.py

import cv2

img1 = cv2.imread(r"assets/1_Gammar 2021_1_2021_06_03-13-19-23-856.PNG")
img2 = cv2.imread(r"assets/1_Limniu 2021_1_2021_06_02-13-08-37-941.PNG")
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

added = cv2.add(img1, img2_resized)
subtracted = cv2.subtract(img1, img2_resized)

cv2.imshow("Added Image", added)
cv2.imshow("Subtracted Image", subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()

