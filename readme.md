# Navigation Stack for Create Robot and Rplidar

## Usage Instructions

### System Requirements
- Ubuntu 20.04
- ROS 1 Noetic

### Installation Steps
1. **Install Turtlebot3 Packages:** Ensure that the Turtlebot3 packages are installed on your system.

2. **Clone Repository**

Clone the repository to your ROS workspace (`src` folder).

```
git clone https://github.com/SwxTemp/TECHIN517_Navigation.git
```

3. **Update USB Serial Port Names:**
- Navigate to the following files:
  - `create_robot/create_bringup/config/default.yaml`
  - `rplidar_ros/launch/rplidar_a1.launch`
- Update the USB serial port names as needed. Typically, one is named USB1 and the other is named USB0.

4. **Build Workspace:**

```bash
catkin build
```

Build your ROS workspace.

If you encounter any errors, try clean the workspace and build again:

```bash
catkin clean
```

### Running the Navigation System

1. **Launch Navigation System:**

```
roslaunch create_navigation create_navigation.launch
```

2. This launch command will automatically perform the following tasks:
- Initialize the lidar a1
- Start the iRobot Create2
- Launch the Map Server
- Run the AMCL (Adaptive Monte Carlo Localization) Node
- Activate the Move Base
- Launch Rviz for visualization


## Running the Simulation

```bash
roscore
```

```bash
roslaunch create_gazebo create_world.launch
```

```bash
roslaunch create_navigation create_navigation.launch map_file:=$HOME/map/gix_map_2f.yaml

```

- The default world model is `gix-2f` that you can get in world folder

- The default map_file is `gix_map_2f.yaml` and `gix_map_2f.pgm`

- Remember to change the map_file with your local file position

- You can also use the following command to visualize robot in Rviz: `roslaunch create_gazebo create_gazebo_rviz.launch`

- And then use teleop tool to control the robot: `roslaunch create_teleop create_teleop.launch`


## How to use creat_slam to build map

### In simulation
- Open a world model: `roslaunch create_gazebo create_world.launch`
- Run slam launch file: `roslaunch create_slam create_slam.launch slam_methods:=gmapping`
- Control robot move: `roslaunch create_teleop create_teleop.launch`
- Save the map: `rosrun map_server map_saver -f ~/path/to/save`

### Use physical robot
- Connect with the physical robot
- Run slam launch file: `roslaunch create_slam create_slam.launch slam_methods:=gmapping`
- Control robot move: `roslaunch create_teleop create_teleop.launch`
- Save the map: `rosrun map_server map_saver -f ~/path/to/save`

<!-- ## How to use

1. Using Ubuntu 20.04 and ROS 1 Noetic
2. Install turtlebot3 pakages
3. git clone this repo under src folder
4. Change USB serial port name in
  1. `create_robot/create_bringup/config/default.yaml`
  2. `rplidar_ros/launch/rplidar_a1.launch`
  3. Note that it is normally one is USB1 and the other is USB0
5. `catkin_make` under your ws folder
6. Run
  `roslaunch create_navigation create_navigation.launch`
7. This will automatically do such things:
  1. Run bringup for lidar
  2. Run bringup for create2
  3. Run Map Server
  4. Run AMCL Node
  5. Run Move base
  6. Run Rviz -->

# Use Raspberry Pi to drive robot and laptop to navigate

### **Prerequisites**

- Ensure ROS is installed on both the Raspberry Pi and the laptop. This guide assumes you are using ROS Noetic.
- Both devices must be connected to the same network.

### **Network Configuration**

### **Step 1: Determine IP Addresses**

On both the Raspberry Pi and the laptop, open a terminal and run:

```bash

hostname -I
```

Note down the IP addresses displayed.

### **Step 2: Configure Environment Variables**

On both devices, you will need to set up the ROS network environment variables in the **`~/.bashrc`** file.

### On Raspberry Pi (ROS Master)

Add the following lines to **`~/.bashrc`**:

```bash
export ROS_MASTER_URI=http://[Pi_IP_address]:11311
export ROS_HOSTNAME=[Pi_IP_address]

```

Replace **`[Pi_IP_address]`** with the IP address noted earlier.

### On Laptop (ROS Node)

Add the following lines to **`~/.bashrc`**:

```bash
export ROS_MASTER_URI=http://[Pi_IP_address]:11311
export ROS_HOSTNAME=[Laptop_IP_address]
```

Replace **`[Pi_IP_address]`** and **`[Laptop_IP_address]`** with their respective IP addresses.

After modifying **`~/.bashrc`**, apply the changes by running:

```bash
source ~/.bashrc
```

on both devices.

### **Step 3: Verify Network Configuration**

Ensure that both devices can communicate with each other via the ROS master. On the laptop, you can check if it can see the ROS master by running:

```bash
rostopic list
```

This command should return a list of active ROS topics if the network is configured correctly.

### **Running the Launch Files**

### **On Raspberry Pi**

First **Update USB Serial Port Names**: 
- Navigate to the following files:
  - `create_robot/create_bringup/config/default.yaml`
  - `rplidar_ros/launch/rplidar_a1.launch`

Navigate to the directory containing the **`pi_launch.launch`** file and run:

```bash
roslaunch create_navigation pi_launch.launch
```

### **On Laptop**

Navigate to the directory containing the **`laptop_launch.launch`** file and run:

```bash
roslaunch create_navigation laptop_launch.launch
```

### **Troubleshooting**

- **Unable to Communicate Between Devices**: Check if both devices have the correct IP settings in **`~/.bashrc`** and are on the same network. Also, ensure there are no firewall settings blocking the necessary ports (especially 11311).
- **Commands Not Recognized**: Ensure that ROS is properly installed and that you have sourced the setup file in **`~/.bashrc`** with:or the appropriate path for your ROS installation.
    
    ```bash
    source /opt/ros/noetic/setup.bash
    
    ```