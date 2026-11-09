import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('lenna.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('ex1.png')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

dft1 = cv2.dft(np.float32(gray1), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift1 = np.fft.fftshift(dft1)
out1 = 20*np.log(cv2.magnitude(dft_shift1[:, :, 0], dft_shift1[:, :, 1]))
out2 = cv2.phase(dft1[:, :, 0], dft1[:, :, 1])

dft2 = cv2.dft(np.float32(gray2), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift2 = np.fft.fftshift(dft2)
out3 = 20*np.log(cv2.magnitude(dft_shift2[:, :, 0], dft_shift2[:, :, 1]))
out4 = cv2.phase(dft2[:, :, 0], dft2[:, :, 1])

plt.subplot(221), plt.imshow(out1, cmap='gray')
plt.title('CameraMan Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(out2, cmap='gray')
plt.title('CameraMan Phase Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(out3, cmap='gray')
plt.title('Blocks Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(out4, cmap='gray')
plt.title('Blocks Phase Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()