import cv2

img = cv2.imread("resources/test.jpg")
# make a copy of the original image

halfEllipse = img.copy()

# define the center of half ellipse

ellipse_center = (415, 190)
# define the axis point
axis1 = (100, 50)
# draw the Incomplete/Open ellipse, just a outline
cv2.ellipse(halfEllipse, ellipse_center, axis1,
            0, 180, 360, (255, 0, 0), thickness=3)
# if you want to draw a Filled ellipse, use this line of code
cv2.ellipse(halfEllipse, ellipse_center, axis1,
            0, 0, 180, (0, 0, 255), thickness=-2)
# display the output
cv2.imshow('halfEllipse', halfEllipse)
cv2.waitKey(0)
