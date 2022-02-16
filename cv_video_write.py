import cv2 as cv


vid_capture = cv.VideoCapture('resources/test.mp4')

if (vid_capture.isOpened() == False):
    print(f'Failed to open the file!!!')

frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width, frame_height)
fps = 20

output = cv.VideoWriter("resources/output_video.avi",
                        cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, frame_size)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        output.write(frame)
    else:
        print('Stream Disconnected')
        break