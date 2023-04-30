#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import math
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from tf import transformations
from std_srvs.srv import *
import time
from assignment_2_2022.msg import nodeA

# Brings in the SimpleActionClient
import actionlib
import actionlib_msgs
import assignment_2_2022.msg


def msg_callback(info):
 pub = rospy.Publisher('chatter', nodeA, queue_size=10)#create pub object to publish in the nodeA
 #while not rospy.is_shutdown():
 message=nodeA()#message will have the properties of the nodeA() msg
 message.x=info.pose.pose.position.x
 message.y=info.pose.pose.position.y
 message.velx=info.twist.twist.linear.x
 message.vely=info.twist.twist.linear.y
 
 #in message assign the position and velocity in (X,Y) each time in the simulation
 
 print(message)
 rate = rospy.Rate(20) # Set a publish rate
 pub.publish(message) #publish in the topic nodeA
 rate.sleep()
  

#main program
if __name__ == '__main__':
    try:
        # Initializes a rospy node
        rospy.init_node('nodeAmsg')
        rospy.Subscriber("/odom", Odometry, msg_callback)#subscribe to the topic /odom, and call the function msg_callback
        rospy.spin()#keep the program working until the .py finishes
        
       
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
