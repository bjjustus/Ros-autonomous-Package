#!/usr/bin/env python

import rospy, math
from geometry_msgs.msg import Twist
from adafruit_servokit import ServoKit
import adafruit_motor.servo

msg=Twist()
#initialize kit
kit = ServoKit(channels=16) 

#def convert_trans_rot_vel_to_steering_angle(omega):
#    #turns angular.z value into an angle
#    return 12*omega+90

def callback(msg):
#    x=msg.linear.x
    z=msg.angular.z
    steering = 12*z+90
    print(steering)
    #add steering
    kit.servo[1].angle = steering
def driver():
    #subscriber gets cmd_vel values from open cv file
    rospy.init_node('car')
    rospy.Subscriber('/cmd_vel', Twist, callback)
    kit.continuous_servo[2].throttle = 0.05
    rospy.spin()
    
	
#insert throttle
driver()
