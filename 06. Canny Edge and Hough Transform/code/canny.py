import cv2
import numpy as np

img = cv2.imread('mine1.jpg')
img2 = img.copy()
# 그레이 스케일로 변환 및 엣지 검출 ---①
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur  = cv2.GaussianBlur(imgray, (7, 7), 2, 2)
edges = cv2.Canny(blur, 50, 200)

# 확율 허프 변환 적용 ---②
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, None, 110, 3)
for line in lines:
    # 검출된 선 그리기 ---③
    x1, y1, x2, y2 = line[0]
    cv2.line(img2, (x1,y1), (x2, y2), (0,255,0), 1)

cv2.imshow('Probability hough line', img2)
cv2.imshow('canny',edges)
cv2.waitKey()
cv2.destroyAllWindows()