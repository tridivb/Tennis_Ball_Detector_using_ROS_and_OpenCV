# Tennis_Ball_Detector_using_ROS_and_OpenCV

### Dependencies:
Ros-Kinetic <br>
Python <br>
OpenCV

### Goal
This was done as part of the exercises of the Udemy course [ROS for Beginners: Basics, Motion, and OpenCV](https://www.udemy.com/ros-essentials/learn/v4/overview) by Anis Koubaa. <br>
It is an example of a ROS publisher and listener. Here the publisher reads a video file and publishes each frame. The listener in turn reads each frame and tries to detect the tennis ball (if any) in it.

### Remarks
Since this is primarily an example of a publisher and listener interacting, the detector section is very basic. The detection can be improved by applying erosion and dilution. The color calbration is also presently done for the lighting conditions in the video. The ball detector code was tested with a USB camera as well but expectedly is very sensitive to conditions different from that in the video.

**Screenshot from Test with Video** <br>
![ROS for Beginners: Basics, Motion, and OpenCV](https://www.udemy.com/ros-essentials/learn/v4/overview)

**Screenshot from Test with USB Cam** <br>
![ROS for Beginners: Basics, Motion, and OpenCV](https://www.udemy.com/ros-essentials/learn/v4/overview)
