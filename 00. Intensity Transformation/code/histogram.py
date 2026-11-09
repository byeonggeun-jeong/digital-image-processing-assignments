import cv2
import matplotlib.pyplot as plt

src = cv2.imread('pollen.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([src], [0], None, [256], [0,255])

plt.plot(hist)
plt.show()