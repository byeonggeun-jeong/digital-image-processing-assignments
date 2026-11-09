import matplotlib.pyplot as plt
import cv2

img = cv2.imread('island.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

out=gray.copy()

height, width = gray.shape

def fun1(x,r1,s1):
    return x * (s1/r1)

def fun2(x,r1,r2,s1,s2):
    return (x-r1) * ((s2-s1)/(r2-r1)) + s1

def fun3(x,r2,s2):
    return (x-r2) * ((255-s2)/(255-r2)) + s2

for i in range(0, height):
    for j in range(0, width):
        if gray[i][j] >= 0 and gray[i][j] <=109:
            out[i][j] = round(fun1(gray[i][j],110,70))
        elif gray[i][j] >= 110 and gray[i][j] <= 139:
            out[i][j] = round(fun2(gray[i][j],110,140,70,180))
        elif gray[i][j] >= 140 and gray[i][j] <= 255:
            out[i][j] = round(fun3(gray[i][j],140,180))

cv2.imshow("original", gray)
cv2.imshow("stretching", out)

plt.figure()

plt.subplot(1, 2, 1)
plt.hist(gray.ravel(), 256, [0, 255])

plt.subplot(1, 2, 2)
plt.hist(out.ravel(), 256, [0, 255])


plt.show()