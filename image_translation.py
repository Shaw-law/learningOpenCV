import cv2 as cv
import numpy as np

image = cv.imread('resources/image.webp')

height, width = image.shape[:2]

tx, ty = width/4, height/4

translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype = np.float32)

translated_image = cv.warpAffine(
    src=image, M=translation_matrix, dsize=(width, height))

cv.imshow("Translated Image", translated_image)
cv.imshow("Original Image", image)

cv.waitKey(0)
cv.imwrite('translated_image.webp', translated_image)
cv.destroyAllWindows()
