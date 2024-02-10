#!/usr/bin/env python

import rospy
from your_package_name.msg import StringIntFloatBool  # Import the custom message type

def publisher_node():
    # Initialize the ROS node
    rospy.init_node('my_publisher_node', anonymous=True)

    # Create a publisher with topic name 'my_topic' and message type 'StringIntFloatBool'
    pub = rospy.Publisher('my_topic', StringIntFloatBool, queue_size=10)

    # Set the publishing rate (1 Hz in this example)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # Create a StringIntFloatBool message and publish it
        message = StringIntFloatBool()
        message.string_data = 'Hello, ROS!'
        message.int_data = 42  # Replace with your integer data
        message.float_data = 3.14  # Replace with your float data
        message.bool_data = True  # Replace with your boolean data
        pub.publish(message)

        # Wait according to the specified rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass
