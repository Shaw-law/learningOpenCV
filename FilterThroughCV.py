import cv2 as cv
import numpy as np
from numpy.core.numeric import identity

image = cv.imread('resources/test.jpg')

if image is None:
    print('Could not read the image')


# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv.imshow('Original', image)
cv.imshow('Identity', identity)

cv.waitKey()
cv.imwrite('identity.jpg', identity)
cv.destroyAllWindows()

# Apply Kernel Image
kernel2 = np.ones((5,5), np.float32a) / 25
img = cv.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv.imshow('Original', image)
cv.imshow('Kernel Image', img)

cv.waitKey()
cv.imwrite('blur_kernel.jpg', img)
cv.destroyAllWindows()
