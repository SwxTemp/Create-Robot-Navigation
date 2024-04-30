#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import math

def publish_scan():
    rospy.init_node('rplidar_simulator', anonymous=True)
    pub = rospy.Publisher('/scan', LaserScan, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        scan = LaserScan()
        scan.header.stamp = current_time
        scan.header.frame_id = 'laser_frame'
        scan.angle_min = -math.pi
        scan.angle_max = math.pi
        scan.angle_increment = math.pi / 180
        scan.time_increment = (1.0 / 40) / 360
        scan.range_min = 0.12
        scan.range_max = 10.0

        # Simulate a wall at 1 meter in front of the robot
        ranges = [float('inf')] * 360
        # Set ranges from 80 degrees to 100 degrees to 1 meter
        for i in range(80, 101):
            ranges[i] = 1.0  # wall at 1 meter

        scan.ranges = ranges
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_scan()
    except rospy.ROSInterruptException:
        pass
