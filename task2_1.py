# task2_1.py

import cv2

image = cv2.imread(r"assets/1_Gammar 2021_1_2021_06_03-13-19-23-856.PNG")
print("Type of the image array:", type(image))

if image is not None:
    print("Shape of the image array:", image.shape)
else:
    print("Image could not be read.")

