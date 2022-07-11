import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_path",help="path to the video file")
args = parser.parse_args()

capture = cv2.VideoCapture(args.video_path)

if capture.isOpened() == False:
    print("Error opening video file")

# 拿到视频的总帧数
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print("Starting in frame:{}".format(frame_index))

while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_FRAME_COUNT,frame_index)
    ret,frame = capture.read()

    if ret:
        cv2.imshow("Original frame",frame)
        frame_index= frame_index-1
        print("Next index to read:{}".format(frame_index))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()