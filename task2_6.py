# task2_6.py

import cv2

image = cv2.imread(r"assets/1_Gammar 2021_1_2021_06_03-13-19-23-856.PNG")
print("Original pixel value:", image[50, 50])
image[50, 50] = [255, 255, 255]
cv2.imwrite("modified.png", image)

