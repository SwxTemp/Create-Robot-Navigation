# How to use creat_slam to build map

## In simulation
- Open a world model: `roslaunch create_gazebo create_world.launch`
- Run slam launch file: `roslaunch create_slam create_slam.launch slam_methods:=gmapping`
- Control robot move: `roslaunch create_teleop create_teleop.launch`
- Save the map: `rosrun map_server map_saver -f ~/path/to/save`

## Use physical robot
- Connect with the physical robot
- Run slam launch file: `roslaunch create_slam create_slam.launch slam_methods:=gmapping`
- Control robot move: `roslaunch create_teleop create_teleop.launch`
- Save the map: `rosrun map_server map_saver -f ~/path/to/save`
