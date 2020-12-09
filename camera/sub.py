#!/usr/bin/env python

import rospy, math
from geometry_msgs.msg import Twist

def callback(data):
     rospy.loginfo(data.data)
def listener():
         rospy.init_node('listener', anonymous=True)
  
         rospy.Subscriber("/cmd_vel", Twist, callback)
  
       # spin() simply keeps python from exiting until this node is stopped
         rospy.spin()
   
if __name__ == '__main__':
       listener()
