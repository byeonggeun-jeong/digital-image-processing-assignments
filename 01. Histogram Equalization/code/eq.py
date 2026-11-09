import cv2
from matplotlib import pyplot as plt

img = cv2.imread('7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist1 = cv2.equalizeHist(gray)


cv2.imshow("original", gray)
cv2.imshow("result1", hist1)

plt.figure()
plt.subplot(1,2,1)
plt.hist(img.ravel(), 256, [0, 256])
plt.subplot(1,2,2)
plt.hist(hist1.ravel(), 256, [0, 256])

plt.show()