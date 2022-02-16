
import cv2 as cv

img = cv.imread('resources/test.jpg')

cv.imshow("Original Image", img)
#cv.waitKey(0)

#if img is None:
#    print("Could not read the Image")

imageLine = img.copy()

# Draw the Image from point A to B

pointA = (200, 80)
pointB = (450, 80)

cv.line(imageLine, pointA, pointB, (255, 255, 0),
        thickness=3, lineType=cv.LINE_AA)

cv.imshow("Image Line", imageLine)
cv.waitKey(0)
