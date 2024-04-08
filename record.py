import cv2

def get_rtsp_frame_size(rtsp_url):
    # Open RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    # Check if the stream is opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open the video stream.")
        return None

    # Read the first frame
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read the frame.")
        return None

    # Get frame size
    frame_size = (frame.shape[1], frame.shape[0])

    # Release the capture
    cap.release()

    return frame_size

# RTSP URL of the video stream
rtsp_url = 'your_rtsp_url_here'

# Get frame size
frame_size = get_rtsp_frame_size(rtsp_url)

if frame_size:
    print("Frame Size:", frame_size)
else:
    print("Failed to retrieve frame size.")
