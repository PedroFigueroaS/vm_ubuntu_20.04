#!/usr/bin/env python
import rospy
import math
from assignment_2_2022.msg import nodeA
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped


euc_dist=0
euc_vel=0
def callback(msg):
#while not rospy.is_shutdown():
    pxd=rospy.get_param("/des_pos_x")
    pyd=rospy.get_param("/des_pos_y")
    #get the target position from the rospy parameters
    px=msg.x
    py=msg.y
    velx=msg.velx
    vely=msg.vely
    #get the posx, posy, velx, vely from the msg object
    euc_dist=math.sqrt(((pxd-px)**2)+((pyd-py)**2))#compute the euclidean distance
    euc_vel=math.sqrt(((velx)**2)+((vely)**2))#compute the euclidean velocity
    print("Distance:",euc_dist, end=" ")#print the distance
    print("velx:",euc_vel)#print the velocity

    
#main function
if __name__ == '__main__':
    # Initializes a rospy node
    rospy.init_node('nodeC')
    rospy.Subscriber("chatter", nodeA, callback)#subscribe to the chatter topic, with the type of message of nodeA, and call the callback function
    rospy.spin()#keep the program working until python terminates it

