import rospy
from geometry_msgs.msg import Twist

class MoveRobot:
    def __init__(self):
        rospy.init_node('move_robot')
        self.publisher_ = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz
        self.twist_msg = Twist()

    def publish_twist(self):
        # Set linear.x and angular.z to control the robot's motion
        self.twist_msg.linear.x = 0.1 # Move forward at 0.5 m/s
        self.twist_msg.angular.z = 0.2  # Rotate counter-clockwise at 0.2 rad/s
        # print("sent", self.twist_msg)
        self.publisher_.publish(self.twist_msg)
        self.rate.sleep()

def main():
    move_robot = MoveRobot()
    while not rospy.is_shutdown():
        move_robot.publish_twist()

if __name__ == '__main__':
    main()
