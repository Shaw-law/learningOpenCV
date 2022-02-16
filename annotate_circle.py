import cv2 as cv

img = cv.imread("resources/test.jpg")

imageCircle = img.copy()

circle_center = (415, 190)
radius = 100

# cv.circle(imageCircle, circle_center, radius,
#          (0, 0, 255), thickness=3, lineType=cv.LINE_AA)
#
#cv.imshow("Circle Annotate", imageCircle)

imageWithFilledCircle = img.copy()

cv.circle(imageWithFilledCircle, circle_center, radius,
          (255, 255, 0), thickness=-1, lineType=cv.LINE_AA)

cv.imshow("Filled Image", imageWithFilledCircle)

cv.waitKey(0)
