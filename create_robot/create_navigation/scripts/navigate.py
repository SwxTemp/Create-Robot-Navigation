#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def send_goal(x, y, z, w):
    rospy.init_node('send_goal_node')

    # Create an action client
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Define the goal
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    # Send the goal
    client.send_goal(goal)
    client.wait_for_result()

    # Check if the robot reached its goal
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("The robot has reached the goal")
    else:
        rospy.loginfo("The robot failed to reach the goal")

    # Publish the goal for RViz
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    goal_msg = PoseStamped()
    goal_msg.header.frame_id = "map"
    goal_msg.header.stamp = rospy.Time.now()
    goal_msg.pose.position.x = x
    goal_msg.pose.position.y = y
    goal_msg.pose.orientation.z = z
    goal_msg.pose.orientation.w = w

    rospy.sleep(1)  # Allow some time for the publisher to set up
    pub.publish(goal_msg)
    rospy.loginfo("Goal published to /move_base_simple/goal")


if __name__ == '__main__':
    try:
        x = 16.1278
        y = -32.83

        # jiang zhuo
        # x = 25.57
        # y = -25.95
        
        z = -1.0
        w = 0.0
        result = send_goal(x, y, z, w)
        if result:
            rospy.loginfo("Navigation success!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Program terminated.")
