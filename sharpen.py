import cv2 as cv
import numpy as np
from numpy.core.numeric import identity

image = cv.imread('resources/wood.jpg')

'''
Apply Kernel Identity
'''

'''
#kernel1 = np.array([[0,0,0],
                    [0,1,0],
                    [0,0,0]])
'''

# filter2D() fuction can be used to apply kernel to an image
# where ddepth is the desired depth of an image
# ddepth -1 if orginal depth
#identity = cv.filter2D(image, ddepth=-1, kernel=kernel1)
'''
# We should get the same image
cv.imshow('Original Image', image)
#cv.imshow("Identity image", identity)

kernel2 = np.ones((5, 5), np.float32) / 5
img = cv.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv.imshow('Kernel Blur', img)
'''

'''
Apply Gaussian blur
'''

# sigmaX is Gaussian Kernel Standard deviation
# ksize is kernel size

gaussian_blur = cv.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)
cv.imshow('Original', image)
cv.imshow('Blurred', gaussian_blur)



cv.waitKey()
cv.imwrite('gaussian_blur_image.jpg', img)
cv.destroyAllWindows()
