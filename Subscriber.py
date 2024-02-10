#!/usr/bin/env python

import rospy
from your_package_name.msg import StringIntFloatBool  # Import the custom message type

def callback(data):
    # Callback function to process received messages
    rospy.loginfo("Received Data:")
    rospy.loginfo("String: %s", data.string_data)
    rospy.loginfo("Integer: %d", data.int_data)
    rospy.loginfo("Float: %f", data.float_data)
    rospy.loginfo("Boolean: %s", data.bool_data)

def subscriber_node():
    # Initialize the ROS node
    rospy.init_node('my_subscriber_node', anonymous=True)

    # Create a subscriber with topic name 'my_topic' and message type 'StringIntFloatBool'
    rospy.Subscriber('my_topic', StringIntFloatBool, callback)

    # Spin to keep the script alive and receive messages
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass
