import cv2

videoCapture = cv2.VideoCapture('Media/MyInputVid.avi')

fps = videoCapture.get(cv2.CAP_PROP_FPS)

size = (int (videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get (cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('Media/MyOutputVid.avi',
                               cv2.VideoWriter_fourcc('I','4', '2', '0'), fps, size)

success, frame = videoCapture.read()
# Loop until there are no more frames.
while success: 
    videoWriter.write(frame)
    success, frame = videoCapture.read()
