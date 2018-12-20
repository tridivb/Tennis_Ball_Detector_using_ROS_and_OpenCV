#!/usr/bin/env python

import cv2
import rospy
from ball_detector import BallDetector
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class CamStreamer:
    def __init__(self):
        rospy.init_node('ball_cam_tracker', anonymous=True)
        self.streamSubscriber = rospy.Subscriber("/usb_cam/image_raw", Image, self.convertCamStream)
        self.detector = BallDetector()
        self.cvVidStream = cv2.VideoCapture(0)
        self.rosToCVBridge = CvBridge()
        self.detector = BallDetector()
    
    # Helper function to convert USB cam stream from ROS to OpenCV format,
    # detect the ball and display the feed
    def convertCamStream(self, rosStream):
        try:
            cvStream = self.rosToCVBridge.imgmsg_to_cv2(rosStream, 'bgr8')
        except CvBridgeError as error:
            print(error)

        maskImage = self.detector.getMask(cvStream, (30, 150, 100), (50, 255, 255))
        contours = self.detector.getContour(maskImage)
        self.detector.drawBallContour(cvStream, contours)
        cv2.imshow("CV Stream", cvStream)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            self.streamSubscriber.unregister()
            cv2.destroyAllWindows()
        
def main():
    streamer = CamStreamer()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Exit Code")

if __name__ == '__main__':
    main()