cmake_minimum_required(VERSION 3.8)
project(ball_follower)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(behaviortree_cpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

#Added C++ Launch 
install(
  # Which folders to copy from src to install
  DIRECTORY config description launch worlds maps bt_xml include
  # Destination install/share
  DESTINATION share/${PROJECT_NAME}
)

#Set Parameters
set(BEHAVIOR_SOURCES
src/navigation_behaviors.cpp
)

set(TARGET_DEPENDS
  ament_cmake
  rclcpp
  sensor_msgs
  nav_msgs
  nav2_msgs
  # behaviortree_cpp
  rclcpp_action
  yaml-cpp
  tf2
  tf2_geometry_msgs
)

#header directory
include_directories(include)

#add library
# add_library(autonomy_node src/autonomy_node.cpp ${BEHAVIOR_SOURCES})  # Assuming source files are in src/
# add_library(navigation_behaviors src/navigation_behaviors.cpp)  # Assuming source file is in src/

# add_executable(bot_node src/bot_node.cpp)
add_executable(laser_remapper_node src/laser_remapper.cpp)
add_executable(map_publisher_node src/map_publisher.cpp)
add_executable(autonomy_node src/autonomy_node.cpp ${BEHAVIOR_SOURCES})
# add_executable(navigation_behaviors src/navigation_behaviors.cpp)

# target_include_directories(bot_node PUBLIC
#   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#   $<INSTALL_INTERFACE:include>)
ament_target_dependencies(laser_remapper_node rclcpp sensor_msgs)
ament_target_dependencies(map_publisher_node rclcpp nav_msgs)
ament_target_dependencies(autonomy_node ${TARGET_DEPENDS})
# ament_target_dependencies(navigation_behaviors rclcpp behaviortree_cpp)


target_compile_features(laser_remapper_node PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
# target_link_libraries(autonomy_node /usr/local/lib/libbehaviortree_cpp.so)
target_link_libraries(autonomy_node ${YAML_CPP_LIBRARIES} /usr/local/lib/libbehaviortree_cpp.so)
# target_link_libraries(${PROJECT_NAME} behaviortree_cpp)


install(TARGETS
  laser_remapper_node
  map_publisher_node
  autonomy_node
  # navigation_behaviors
  DESTINATION lib/${PROJECT_NAME}
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  find_package(rclcpp REQUIRED)
  find_package(sensor_msgs REQUIRED)
  find_package(nav_msgs REQUIRED)
  find_package(nav2_msgs REQUIRED)
  find_package(behaviortree_cpp REQUIRED)
  find_package(rclcpp_action REQUIRED)
  find_package(yaml-cpp REQUIRED)
  find_package(tf2 REQUIRED)
  find_package(tf2_geometry_msgs REQUIRED)

  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()


ament_package()
