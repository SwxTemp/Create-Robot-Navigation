# How to use navigation simulation

```
roscore
roslaunch create_gazebo create_world.launch
roslaunch create_navigation create_navigation.launch map_file:=$HOME/map/gix_map_2f.yaml
```
- Remember to change the map_file position with your local file

- You can also use the following command to control robot in Rviz: `roslaunch create_gazebo create_gazebo_rviz.launch`

- And then use teleop to control the robot: `roslaunch create_teleop create_teleop.launch`