import cv2 as cv

image = cv.imread('resources/image.webp')

# Dividing height and width by 2 to get center of the image
height, width = image.shape[:2]

# Get the center coordinates of the image to create the 2D array
center = (width/2, height/2)

# using cv.getRotationMatrix2D() to get the rotational matrix
rotate_matrix = cv.getRotationMatrix2D(center = center, angle = 45, scale = 1)

# Rotate the matrix using cv.warpAffine
rotated_image = cv.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

cv.imshow("Original Image", image)
cv.imshow("Rotated Image", rotated_image)

cv.waitKey(0)
cv.destroyAllWindows()