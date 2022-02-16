import cv2 as cv

img = cv.imread("resources/test.jpg")

imageRectangle = img.copy()

start_point = (300, 115)
end_point = (475, 255)

cv.rectangle(imageRectangle, start_point, end_point,
             (0, 0, 255), thickness=3, lineType=cv.LINE_8)

cv.imshow("Rectangle Image", imageRectangle)
cv.waitKey(0)
