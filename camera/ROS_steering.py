#!/usr/bin/env python

import rospy, math
from geometry_msgs.msg import Twist    

msg=Twist()
#initialize kit

def convert_trans_rot_vel_to_steering_angle(omega):
    #turns angular.z value into an angle
    return 12*omega+90

def callback(msg):
    #continously loops function
    #insert throttle output
    while not rospy.is_shutdown():
         x=msg.linear.x
         z=msg.angular.z
         steering = convert_trans_rot_vel_to_steering_angle(z)
	 #insert steering output
         #delete print once we confirm it works
	 print(z)
	 print(steering)

def driver():
    #subscriber gets cmd_vel values from open cv file
    rospy.init_node('car')
    rospy.Subscriber('/cmd_vel', Twist, callback)
    #keeps node open
    rospy.spin()

driver()
