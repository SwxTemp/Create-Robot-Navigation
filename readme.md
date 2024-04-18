# Create 

## 4.16 Update
### 目前进度
- 设置扫地机器人
  - 型号是iRobot Create 2 (同时也是roomba6系列)
  - Link: https://edu.irobot.com/what-we-offer/create-robot 
- 安装依赖环境，实现基本控制
  - 在GIX Laptop上实现了对它的teleop，可以通过topic cmd_vel发送move指令
- 底层控制依赖于Create Robot Repo Driver包 [https://github.com/AutonomyLab/create_robot]
  - 此包依赖ROS2，所以需要在ROS2环境下运行
  - 由于系统是Ubuntu 2004,选择ROS2 Galactic版本
 
### TODO
- 使用树莓派
  - 在树莓派的SD卡上重新安装系统，最好是Ubuntu 2004: https://ubuntu.com/download/raspberry-pi, connect to wifi: https://ubuntuforums.org/showthread.php?t=249654
  - 在树莓派中安装ROS2（其他组使用ROS1，可能还需要设置ROS bridge）: https://docs.ros.org/en/galactic/Installation.html
- 安装雷达
  - 实现雷达与Laptop或者树莓派的正常连接:https://www.youtube.com/watch?v=WVyJjxAyGJc
  - 安装Driver，可以正常使用雷达功能
  - `roslaunch rplidar_ros view_rplidar_a1.launch`
  - 
- 集成树莓派+机器人+雷达
  - 实现基于给定地图的Navi

## Links

Create Robot Repo Driver
https://github.com/AutonomyLab/create_robot 

Create Robot Interface
https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf 

ROS2:
https://docs.ros.org/en/galactic/index.html

做完发现还有一个包是：https://github.com/MomsFriendlyRobotCompany/pycreate2 
不太清楚这个是否可以驱动，留作备用

## Setup Steps for Create 2

- Install ROS2

- Followe instruction in https://github.com/AutonomyLab/create_robot Install

- Build successfully(Remember to set ROS env correctly!)

- Run bringup: `ros2 launch create_bringup create_2.launch`

- Using teleop_test.py to control via cmd_vel topic
