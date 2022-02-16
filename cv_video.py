from importlib import resources
import cv2 as cv

vid_capture = cv.VideoCapture('resources/test.mp4')

if (vid_capture.isOpened() == False):
    print(f'Failed to open the file!!!')
else:
    fps = vid_capture.get(5)
    print('Frames per second: ', fps, 'FPS')

frame_count = vid_capture.get(7)
print('Frame Count: ', frame_count)

while(vid_capture.isOpened()):
    # read() function returs a tuple: first a boolean and second the frame
    ret, frame = vid_capture.read()
    if ret == True:
        cv.imshow("Frame", frame)
        key = cv.waitKey(20)

        if key == ord('q'):
            break
    else:
        break


vid_capture.release()
cv.destroyAllWindows()
