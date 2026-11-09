import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = mpimg.imread('solidWhiteCurve.jpg')

def grayscael(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = grayscael(img)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img,(kernel_size, kernel_size),0)

kernel_size = 5
blur_gray = gaussian_blur(gray, kernel_size)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

low_threshold = 50
high_threshold = 200
edges = canny(blur_gray, low_threshold, high_threshold)

def region_of_interest(img, vertices):
    mask = np.zero_like(img)

    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    cv2.fillPoly(mask, vertices, ignore_mask_color)

    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

imshape = img.shape
vertices = np.array([[(100,imshape[0]),(450,320),(550,320),(imshape[1]-20,imshape[0])]],dytpe=np.int32)
mask = region_of_interest(edges, vertices)

def draw_lines(img, lines, color=[255,0,0], thickness=5)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1,y1), (x2,y1), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
                            minLIneLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0],img.shape[1],3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img, a = 0.8, b = 1., c =0.):
    return cv2.addWeighted(initial_img, a, img, b ,c)
