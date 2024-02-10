#!/usr/bin/env python

import rospy
from your_package_name.msg import StringIntFloatBool  # Import the custom message type

def get_user_input():
    string_data = input("Enter a string: ")
    int_data = int(input("Enter an integer: "))
    float_data = float(input("Enter a float: "))
    bool_data_str = input("Enter a boolean (True/False): ")
    bool_data = bool_data_str.lower() == 'true'

    return string_data, int_data, float_data, bool_data

def publisher_node():
    # Initialize the ROS node
    rospy.init_node('my_publisher_node', anonymous=True)

    # Create a publisher with topic name 'my_topic' and message type 'StringIntFloatBool'
    pub = rospy.Publisher('my_topic', StringIntFloatBool, queue_size=10)

    # Set the publishing rate (1 Hz in this example)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # Get user input
        string_data, int_data, float_data, bool_data = get_user_input()

        # Create a StringIntFloatBool message and publish it
        message = StringIntFloatBool()
        message.string_data = string_data
        message.int_data = int_data
        message.float_data = float_data
        message.bool_data = bool_data
        pub.publish(message)

        # Wait according to the specified rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass
