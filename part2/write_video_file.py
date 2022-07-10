# author: xwwwb
# date: 2022-07-11
# description: 创建并保存视频文件
import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("output_video_path",
                    help="path to the video file to write")
args = parser.parse_args()

capture = cv2.VideoCapture(0)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

