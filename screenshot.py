import cv2

def take_a_pic():
    count = 0
    video_capture = cv2.VideoCapture(0)
    # Check success
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = video_capture.read()
    name = "frame%d.jpg" % count
    pic = cv2.imwrite(name, frame)  # save frame as JPEG file
    count += 1

