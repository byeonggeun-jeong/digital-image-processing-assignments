import matplotlib.pyplot as plt
import cv2

img = cv2.imread('pollen.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

out=gray.copy()

height, width = gray.shape

def gamma(x,a,b,c,d,r):
    return round(((x-a)/(b-a)) ** r * (d-c) + c)

for i in range(0, height):
    for j in range(0, width):
        if gray[i][j] >= 115 and gray[i][j] <= 134:
            out[i][j] = gamma(gray[i][j], 115, 135, 115, 135, 0.7)
        else:
            out[i][j] = gray[i][j]

cv2.imshow("original", gray)
cv2.imshow("gamma", out)

plt.figure()

plt.subplot(1, 1, 1)
plt.hist(gray.ravel(), 256, [0, 255])

plt.show()
