# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "tf;gazebo_ros;gazebo_plugins;roscpp;sensor_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lgazebo_ros_velodyne_laser".split(';') if "-lgazebo_ros_velodyne_laser" != "" else []
PROJECT_NAME = "velodyne_gazebo_plugins"
PROJECT_SPACE_DIR = "/home/ikebe/turtlebot3_ws/install"
PROJECT_VERSION = "1.0.2"
