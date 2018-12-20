cmake_minimum_required(VERSION 2.8.3)
project(ros_service_assignment)

find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs message_generation)

## Generate added messages and services with any dependencies listed here
generate_messages( DEPENDENCIES std_msgs )


## Declare a catkin package
catkin_package(CATKIN_DEPENDS message_runtime)
