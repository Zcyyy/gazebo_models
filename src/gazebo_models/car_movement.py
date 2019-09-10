#!/usr/bin/env python
from __future__ import print_function

import rospy
import sys
from geometry_msgs.msg import Twist

# this script is used to control the car. ONLY for test usage. WILL be replaced by the Zcyyy's navigation model soon.

class car_vel_controller():
    def __init__(self):
        self.vel_pub = rospy.Publisher("/mybot_cmd_vel", Twist, queue_size=2)
    def perform(self):
        new_vel = Twist()
        seconds = rospy.Time.now().secs
        res = seconds % 6
        if res == 0 or res == 1:
            new_vel.linear.x = 0.5
        elif res == 2 or res == 3:
            new_vel.angular.z = 1
        else: #res == 4 or res == 5
            new_vel.linear.x = -0.5
        self.vel_pub.publish(new_vel)

def main():
    rospy.init_node("car_vel_changer")
    car = car_vel_controller()
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        try:
            car.perform()
            rate.sleep()
        except KeyboardInterrupt:
            print("Shutting donw")
if __name__ == "__main__":
    main()
