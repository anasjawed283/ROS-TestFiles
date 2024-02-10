find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  your_package_name  # Add your package as a dependency
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs your_package_name  # Add your package as a dependency
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Generate messages in the 'msg' folder
add_message_files(
  FILES
  StringIntFloatBool.msg
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

# Declare a C++ executable
add_executable(your_publisher_script src/your_publisher_script.cpp)  # Replace with your publisher script name and path
target_link_libraries(your_publisher_script ${catkin_LIBRARIES})

add_executable(your_subscriber_script src/your_subscriber_script.cpp)  # Replace with your subscriber script name and path
target_link_libraries(your_subscriber_script ${catkin_LIBRARIES})
