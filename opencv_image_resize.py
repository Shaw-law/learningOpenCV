import cv2 as cv
import numpy as np

image = cv.imread('resources/test.jpg')
cv.imshow('Original Image', image)

# downscale the image using new width and height
down_height = 300
down_width = 200
down_points = (down_width, down_height)
resized_down = cv.resize(image, down_points, interpolation=cv.INTER_LINEAR)

# upscale the image to new width and height
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv.resize(image, up_points, interpolation=cv.INTER_LINEAR)

cv.imshow('Resized down by defining height and width', resized_down)
cv.waitKey()
cv.imshow('Resized up by defining height and width', resized_up)
cv.waitKey()


# Scaling Up the image 1.2 times by specifying both scaling factors
scale_up_x = 1.2
scale_up_y = 1.2
# Scaling Down the image 0.6 times specifying a single scale factor.
scale_down = 0.6

scaled_f_down = cv.resize(image, None, fx=scale_down,
                          fy=scale_down, interpolation=cv.INTER_LINEAR)
scaled_f_up = cv.resize(image, None, fx=scale_up_x,
                        fy=scale_up_y, interpolation=cv.INTER_LINEAR)

cv.imshow('Resized by Scale', scaled_f_down)
cv.waitKey()
cv.imshow('Resized by UpScale', scaled_f_up)
cv.waitKey()

cv.destroyAllWindows()
