#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from ball_detector import BallDetector
import sys

class CVStreamer:
    def __init__(self):
        
        rospy.init_node('tennis_ball_listener', anonymous=True)
        self.rosToCVBridge = CvBridge()
        
        self.detector = BallDetector()

    # Helper function to read each frame in ROS format,
    # convert to openCV format, process each frame and display it
    def displayFrame(self, rosFrame):
        
        cvFrame = self.rosToCVBridge.imgmsg_to_cv2(rosFrame, 'bgr8')
        maskImage = self.detector.getMask(cvFrame, (30, 150, 100), (50, 255, 255))
        contours = self.detector.getContour(maskImage)
        self.detector.drawBallContour(cvFrame, contours)
        cv2.imshow("Video", cvFrame)
        if (cv2.waitKey(1) & 0XFF == ord('q')):
            rospy.signal_shutdown("Exit Code")

    def tennis_ball_listener(self):

        rospy.Subscriber('tennis_ball_image', Image, self.displayFrame)

        try:
            rospy.spin()
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    streamer = CVStreamer()
    streamer.tennis_ball_listener()
