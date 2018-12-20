#!/usr/bin/env python

import rospy
import cv2

class BallDetector:

    # Helper function to extract binary mask from image
    def getMask(self, rgbImage, lowerBoundColor, upperBoundColor):
        hsvImage = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvImage, lowerBoundColor, upperBoundColor)
        return mask

    # Helper function to extract contours from image
    def getContour(self, maskImage):
        _, contours, hierarchy = cv2.findContours(maskImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    # Helper function to draw circles around contours in image
    def drawBallContour(self, rgbImage, contours):
        for c in contours:
            if (cv2.contourArea(c) > 100):
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                cv2.drawContours(rgbImage, [c], -1, (150, 250, 150), 1)
                cx, cy = self.getContourCentre(c)
                cv2.circle(rgbImage, (cx, cy), int(radius), (0, 0, 255), 1)
    
    # Helper function to retrieve a contour centre
    def getContourCentre(self, contour):
        moment = cv2.moments(contour)
        cx = None
        cy = None
        if moment['m00'] != 0:
            cx = int(moment['m10'] / moment['m00'])
            cy = int(moment['m01'] / moment['m00'])
        return cx, cy