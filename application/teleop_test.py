
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_twist)
        self.twist_msg = Twist()

    def publish_twist(self):
        # Set linear.x and angular.z to control the robot's motion
        self.twist_msg.linear.x = 0.5  # Move forward at 0.5 m/s
        self.twist_msg.angular.z = 0.2  # Rotate counter-clockwise at 0.2 rad/s
        self.publisher_.publish(self.twist_msg)

def main(args=None):
    rclpy.init(args=args)
    move_robot = MoveRobot()
    rclpy.spin(move_robot)
    move_robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
