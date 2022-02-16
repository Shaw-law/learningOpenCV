import cv2 as cv
import numpy as np

img = cv.imread('resources/test.jpg')
print(img.shape)
cv.imshow("Original Image", img)

# Cropping an Image
cropped_image = img[80:280, 150:330]

# Display Cropped Image
cv.imshow("Cropped Image", cropped_image)

cv.imwrite("Cropped_Image.jpg", cropped_image)

cv.waitKey(0)
cv.destroyAllWindows()