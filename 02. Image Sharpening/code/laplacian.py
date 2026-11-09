import cv2
import numpy as np

img = cv2.imread('figb.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                  [0.04, 0.04, 0.04, 0.04, 0.04],
                  [0.04, 0.04, 0.04, 0.04, 0.04],
                  [0.04, 0.04, 0.04, 0.04, 0.04],
                  [0.04, 0.04, 0.04, 0.04, 0.04]])

kernel = np.ones((5, 5))/5**2

laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

sharpening = np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]]) / 9.0
sharpened = cv2.filter2D(gray, -1, sharpening)

sobel = cv2.Sobel(gray, cv2.CV_8U, 0, 1, 3)

blurred = cv2.filter2D(sobel, -1, kernel)

mask = cv2.addWeighted(gray, 2, blurred, -1, 0)

gamma = mask.copy()
def gamma1(x, a, b, c, d, r):
    return round(((x-a)/(b-a)) ** r * (d-c) + c)

height, width = gray.shape

for i in range(0, height):
    for j in range(0, width):
        gamma[i][j] = gamma1(gamma[i][j], 0, 255, 0, 255, 0.7)

cv2.imshow('original', gray)
cv2.imshow('laplacian', laplacian)
cv2.imshow('sharpened', sharpened)
cv2.imshow('sobel', sobel)
cv2.imshow('blurred', blurred)
cv2.imshow('mask', mask)
cv2.imshow('gamma',gamma)

cv2.waitKey()
cv2.destroyAllWindows()