import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('7.jpg',0);

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img2 = clahe.apply(img)

img = cv2.resize(img,(400,400))
img2 = cv2.resize(img2,(400,400))

dst = np.hstack((img, img2))
cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()

plt.figure()
plt.subplot(1,2,1)
plt.hist(img.ravel(), 256, [0, 256])
plt.subplot(1,2,2)
plt.hist(img2.ravel(), 256, [0, 256])
plt.show()