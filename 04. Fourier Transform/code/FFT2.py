import cv2
import numpy as np

img = cv2.imread('lenna.jpg', 0)
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
mag, phase = cv2.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])
spec = np.log(mag) / 30
mag = cv2.pow(mag, 1.1)
real, imag = cv2.polarToCart(mag, phase)

img2 = cv2.imread('cameraman.tif', 0)
dft2 = cv2.dft(np.float32(img2), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift2 = np.fft.fftshift(dft2)
mag2, phase2 = cv2.cartToPolar(dft_shift2[:,:,0], dft_shift2[:,:,1])
spec2 = np.log(mag2) / 30
mag2 = cv2.pow(mag2, 1.1)

real4, imag4 = cv2.polarToCart(mag, phase2)
back4 = cv2.merge([real4, imag4])
back_ishift4 = np.fft.ifftshift(back4)
img_back3 = cv2.idft(back_ishift4)
img_back3 = cv2.magnitude(img_back3[:,:,0], img_back3[:,:,1])

min3, max3 = np.amin(img_back3, (0,1)), np.amax(img_back3, (0,1))
img_back3 = cv2.normalize(img_back3, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


real4, imag4 = cv2.polarToCart(mag2, phase)
back4 = cv2.merge([real4, imag4])
back_ishift4 = np.fft.ifftshift(back4)
img_back4 = cv2.idft(back_ishift4)
img_back4 = cv2.magnitude(img_back4[:,:,0], img_back4[:,:,1])

min4, max4 = np.amin(img_back4, (0,1)), np.amax(img_back4, (0,1))
img_back4 = cv2.normalize(img_back4, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


cv2.imshow("add1", img_back4)
cv2.imshow("add2", img_back3)
cv2.waitKey(0)
cv2.destroyAllWindows()