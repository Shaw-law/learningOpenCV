import cv2 as cv

img = cv.imread("resources/cat.png")

center = (415, 190)
axis1 = (100, 50)
axis2 = (125, 50)
imageEllipse = img.copy()

cv.ellipse(imageEllipse, center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
cv.ellipse(imageEllipse, center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
cv.imshow("Ellipse Image", imageEllipse)
cv.waitKey(0)
