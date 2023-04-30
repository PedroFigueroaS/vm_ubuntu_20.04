#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time


def callback_position(pose):
    rospy.loginfo("The robot is in %f, %f, %f", pose.x, pose.y, pose.theta)
    
def controller():

    rospy.init_node('controller', anonymous=True)
    rospy.Subscriber("turtle1/pose", Pose, callback_position)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = 0.2
        vel.angular.z= 0.1
        pub.publish(vel)
        #time.sleep(5)
        #vel.linear.x = 0
        #vel.angular.z = 0.5
        #pub.publish(vel)
        #time.sleep(5)
    
if __name__ == '__main__':
    controller()
