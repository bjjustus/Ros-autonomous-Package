#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist




def talker():
	msg=Twist()
        pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
	msg.linear.x=2
	msg.angular.z=2
        while not rospy.is_shutdown():
           
           rospy.loginfo(msg)
           pub.publish(msg)
           rate.sleep()
   
if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass
