#!/usr/bin/env python

import cv2
from ball_detector import BallDetector
import os

class VideoStreamer:
    def __init__(self):
        self.cvVidStream = cv2.VideoCapture(os.path.dirname(os.path.abspath(__file__)) + "/video/tennis-ball-video.mp4")
        self.detector = BallDetector()

    # Helper function to read the video file,
    # detect the ball and display the feed
    def displayOpenCVStream(self):
        while True:
            _, frame = self.cvVidStream.read()
            maskImage = self.detector.getMask(frame, (30, 150, 100), (50, 255, 255))
            contours = self.detector.getContour(maskImage)
            self.detector.drawBallContour(frame, contours)
            cv2.imshow("Video frame", frame)
            if cv2.waitKey(1) & 0XFF == ord('q'):
                break
            
        self.cvVidStream.release()

def main():
    streamer = VideoStreamer()
    streamer.displayOpenCVStream()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
