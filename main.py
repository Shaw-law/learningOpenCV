import cv2 as cv

img_color = cv.imread('cat.png', cv.IMREAD_COLOR)
img_grayScale = cv.imread('cat.png', cv.IMREAD_GRAYSCALE)
img_unchanged = cv.imread('cat.png', cv.IMREAD_UNCHANGED)

cv.imshow('Color Image', img_color)
cv.imshow('GrayScale', img_grayScale)
cv.imshow('unchanged Image', img_unchanged)

cv.waitKey(0)

cv.destroyAllWindows()