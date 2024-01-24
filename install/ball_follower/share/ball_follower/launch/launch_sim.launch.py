import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    package_name="ball_follower"

    # Add Robot State Publisher launch file 
    rsp= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory(package_name),'launch','rsp.launch.py')
            ]
        ), launch_arguments={' use_sim_time':'true', ' use_ros2_control':'false'}.items()
    )

    gazebo_params_file=os.path.join(get_package_share_directory(package_name),'config','gazebo_params.yaml')

    # Add Gazebo launch file from the gazebo installation
    # ros2 launch gazebo_ros gazebo.launch.py
    gazebo= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory('gazebo_ros'),'launch','gazebo.launch.py')
            ]
        ), launch_arguments={'extra_gazebo_args':'--ros-args --params-file '+gazebo_params_file}.items()
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    # ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bot_name

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')


    # diff_drive_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["diff_cont"],
    # )

    # joint_broad_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_broad"],
    # )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        # diff_drive_spawner,
        # joint_broad_spawner
    ])





