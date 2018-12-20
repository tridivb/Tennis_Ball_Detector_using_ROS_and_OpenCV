#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import os
        
class ROSStreamer:
    def __init__(self):
        rospy.init_node('tennis_ball_publisher', anonymous=True)
        
        self.framePublisher = rospy.Publisher('tennis_ball_image', Image, queue_size=10)
        self.cvVidStream = cv2.VideoCapture(os.path.dirname(os.path.abspath(__file__)) + "/video/tennis-ball-video.mp4")
        self.publishRate = rospy.Rate(30)
        self.cvToRosBridge = CvBridge()

    # Helper function to read the video file,
    # convert to ROS format and publish each frame
    def tennis_ball_publisher(self):
        while not rospy.is_shutdown():
            _, frame = self.cvVidStream.read()
            if frame is not None:
                try:
                    rosFrame = self.cvToRosBridge.cv2_to_imgmsg(frame, 'bgr8')
                except CvBridgeError as error:
                    print(error)
                self.framePublisher.publish(rosFrame)
                self.publishRate.sleep()
            else:
                self.cvVidStream = cv2.VideoCapture(os.path.dirname(os.path.abspath(__file__)) + "/video/tennis-ball-video.mp4")
        
        self.cvVidStream.release()

        

if __name__ == '__main__':
    streamer = ROSStreamer()
    
    try:
        streamer.tennis_ball_publisher()
    except rospy.ROSInterruptException:
        pass