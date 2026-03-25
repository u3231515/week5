# task2_7.py

import cv2
import numpy as np

image = cv2.imread(r"assets/1_Gammar 2021_1_2021_06_03-13-19-23-856.PNG")
inverted = 255 - image
combined = np.hstack((image, inverted))
cv2.imshow("Original and Inverted", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

