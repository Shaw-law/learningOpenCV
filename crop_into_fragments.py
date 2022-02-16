import cv2 as cv
import numpy as np

img = cv.imread('resources/test.jpg')
image_copy = img.copy()
image_height = img.shape[0]
image_width = img.shape[1]

M = 76
N = 104
x1 = 0
x1 = 0

for y in range(0, image_height, M):
    for x in range(0, image_width, N):
        if (image_height - y) < M or (image_width - x) < N:
            break
        x1 = y + M
        y1 = x + N

        # Check whether the patched width and height exceeds image width and height
        if x1 >= image_width and y1 >= image_height:
            x1 = image_width - 1
            y1 = image_height - 1
            # Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            # Save each patch in file directory
            cv.imwrite('saved_patches/' + 'title' + str(x) + tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

        elif y1 >= image_height:  # when patch height exceed the image height
            y1 = image_height - 1
            # Crop into patches of MxN
            tiles = image_copy[y:y+M, x:x+N]
            # Save each patch into file directory
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= image_width:  # when patch width exceeds the image width
            x1 = image_width - 1
            # Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            # Save each patch into file directory
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            # Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            # Save each patch into file directory
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
#Save full image into file directory
cv.imshow("Patched Image",img)
cv.imwrite("patched.jpg",img)
cv.waitKey()
cv.destroyAllWindows()