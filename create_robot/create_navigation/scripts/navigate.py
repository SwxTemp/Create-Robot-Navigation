#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion

def move_to_goal(x, y, z, w):
    rospy.init_node('send_navigation_goal', anonymous=False)

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    client.send_goal(goal)
    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        # z = float(input("Enter z coordinate (orientation): "))
        # w = float(input("Enter w coordinate (orientation): "))
        z = 0.0
        w = 1.0
        result = move_to_goal(x, y, z, w)
        if result:
            rospy.loginfo("Navigation success!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Program terminated.")
