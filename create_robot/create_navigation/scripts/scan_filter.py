#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    filtered_scan = LaserScan()
    filtered_scan.header = data.header
    filtered_scan.angle_min = data.angle_min
    filtered_scan.angle_max = data.angle_max
    filtered_scan.angle_increment = data.angle_increment
    filtered_scan.time_increment = data.time_increment
    filtered_scan.scan_time = data.scan_time
    filtered_scan.range_min = data.range_min
    filtered_scan.range_max = data.range_max

    filtered_scan.ranges = [range if range >= 0.3 else float('inf') for range in data.ranges]

    pub.publish(filtered_scan)

def listener():
    rospy.init_node('scan_filter', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback)
    global pub
    pub = rospy.Publisher('/filtered_scan', LaserScan, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
