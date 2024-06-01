#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import math

def distance(p1, p2):
    """Calculate the Euclidean distance between two points"""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def path_callback(path_msg):
    """Callback function for path messages"""
    total_distance = 0.0
    poses = path_msg.poses  # Array of PoseStamped
    if len(poses) > 1:
        for i in range(len(poses) - 1):
            total_distance += distance(poses[i].pose.position, poses[i+1].pose.position)
        rospy.loginfo("Total distance: {:.2f} meters".format(total_distance))

        # Assuming a speed (adjust as needed)
        speed = 0.5  # meters/second
        estimated_time = total_distance / speed
        rospy.loginfo("Estimated time of arrival: {:.2f} seconds".format(estimated_time))

def listener():
    """Setup ROS node and subscriber"""
    rospy.init_node('path_length_calculator', anonymous=True)
    rospy.Subscriber("/move_base/DWAPlannerROS/global_plan", Path, path_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
