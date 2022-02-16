import cv2 as cv

img = cv.imread("resources/test.jpg")

imageText = img.copy()

text = 'I am a woman'

org = (50, 350)

cv.putText(imageText, text, org, fontFace=cv.FONT_HERSHEY_SIMPLEX,
           fontScale=1.5, color=(255, 255, 100))

cv.imshow("Text Image", imageText)
cv.waitKey(0)
cv.destroyAllWindows()
