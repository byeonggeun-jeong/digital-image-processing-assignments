import cv2
import numpy as np

img = cv2.imread('pollen.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = np.array(gray)
gray1 = np.pad(gray1, ((20, 20), (20, 20)), 'symmetric')
height1, width1 = gray1.shape

gau1 = cv2.GaussianBlur(gray1, (99, 99), 16)
gau2 = cv2.GaussianBlur(gray1, (99, 99), 32)
gau3 = cv2.GaussianBlur(gray1, (99, 99), 64)

def max0(x):
    return max(map(max, x))
def min0(x):
    return min(map(min, x))

z1 = gray1/gau1
z1_mean = np.mean(z1)
z1_std = np.std(z1)

start1 = z1_mean - 2 * z1_std
end1 = z1_mean + 2 * z1_std

start10 = min0(z1)
end10 = max0(z1)

for i in range(0, height1):
    for j in range(0, width1):
        if z1[i][j] >= start1 and z1[i][j] <= end1:
            z1[i][j] = (z1[i][j] - start1) / (end1 - start1) * 255
        else:
            z1[i][j] = (z1[i][j] - start10) / (end10 - start10) * 255
        z1[i][j] = round(z1[i][j])

z1 = z1.astype('uint8')

z2 = gray1/gau2
z2_mean = np.mean(z2)
z2_std = np.std(z2)

start2 = z2_mean - 2 * z2_std
end2 = z2_mean + 2 * z2_std

start20 = min0(z2)
end20 = max0(z2)

for i in range(0, height1):
    for j in range(0, width1):
        if z2[i][j] >= start2 and z2[i][j] <= end2:
            z2[i][j] = (z2[i][j] - start2) / (end2 - start2) * 255
        else:
            z2[i][j] = (z2[i][j] - start20) / (end20 - start20) * 255
        z2[i][j] = round(z2[i][j])

z2 = z2.astype('uint8')

z3 = gray1/gau3
z3_mean = np.mean(z3)
z3_std = np.std(z3)

start3 = z3_mean - 2 * z3_std
end3 = z3_mean + 2 * z3_std

start30 = min0(z3)
end30 = max0(z3)

for i in range(0, height1):
    for j in range(0, width1):
        if z3[i][j] >= start3 and z3[i][j] <= end3:
            z3[i][j] = (z3[i][j] - start3) / (end3 - start3) * 255
        else:
            z3[i][j] = (z3[i][j] - start30) / (end30 - start30) * 255
        z3[i][j] = round(z3[i][j])

z3 = z3.astype('uint8')

cv2.imshow('gau1',gau1)
cv2.imshow('gau2',gau2)
cv2.imshow('gau3',gau3)

cv2.waitKey()
cv2.destroyAllWindows()