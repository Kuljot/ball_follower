# Ball Follower
## Gazebo
![image](https://github.com/Kuljot/ball_follower/assets/33811204/3ae810ed-d6a0-4d11-889c-fe0799367f06)

## Go To 
![image](https://github.com/Kuljot/ball_follower/assets/33811204/957b2401-c710-4d7a-ab2c-a549d4e8a0f1)



## Build the Project using
```
colcon build
```

## Launch the Simulation using
```
ros2 launch ball_follower launch_sim.launch.py
```

## Launch the SLAM ToolBox using
```
ros2 launch ball_follower slam.launch.py 
```

## Launch the Teleop Node using
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard 
```

## Save Generated Map using
In RVIZ 
> click on add_new_plugin->Slam_ToolBox_plugin
> Save Map




