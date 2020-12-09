import cv2
import numpy as np
import rospy
from geometry_msgs.msg import Twist


def callback(x):
    pass
    
rospy.init_node('Camera')

cap = cv2.VideoCapture(0)

cv2.namedWindow('sliders')

lowH = 0
highH = 179
lowS = 0
highS = 255
lowV = 0
highV = 255

cv2.createTrackbar('lowH', 'sliders', lowH, 179, callback)
cv2.createTrackbar('highH', 'sliders', highH, 179, callback)

cv2.createTrackbar('lowS', 'sliders', lowS, 255, callback)
cv2.createTrackbar('highS', 'sliders', highS, 255, callback)

cv2.createTrackbar('lowV', 'sliders', lowV, 255, callback)
cv2.createTrackbar('highV', 'sliders', highV, 255, callback)
#publisher
cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move=Twist()
while True:
    # ret, frame = cap.read()
    frame = cv2.imread('image.png')

    # get trackbar positions
    lowH = cv2.getTrackbarPos('lowH', 'sliders')
    highH = cv2.getTrackbarPos('highH', 'sliders')
    lowS = cv2.getTrackbarPos('lowS', 'sliders')
    highS = cv2.getTrackbarPos('highS', 'sliders')
    lowV = cv2.getTrackbarPos('lowV', 'sliders')
    highV = cv2.getTrackbarPos('highV', 'sliders')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([lowH, lowS, lowV])
    higher = np.array([highH, highS, highV])
    #for centroid
    mask = cv2.inRange(hsv, lower, higher)
    h,w,d= frame.shape
    M=cv2.moments(mask)
    #centroid calculation and publisher
    if M['m00']!= 0:
           cx= int(M['m10']/M['m00'])
           cy= int(M['m01']/M['m00'])
           cv2.circle(frame, (cx, cy), 20, (0,0,255), -1)
           err=cx-w/2
           move.linear.x=.1
           move.angular.z=-float(err)/100
           self.cmd_vel_pub.publish(move)
    else:
           cx, cy=0, 0

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    

    key = cv2.waitKey(100) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
