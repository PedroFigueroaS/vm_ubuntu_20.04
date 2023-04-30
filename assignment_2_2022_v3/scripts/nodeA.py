#! /usr/bin/env python

#Import the requires libraries, function, and files
from __future__ import print_function
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

import actionlib
import actionlib_msgs
import assignment_2_2022.msg



def new_position():
 global client #use the same client object created in the main function to connect the action client
 
 
 client.wait_for_server() #wait to connect to the server
 goal=PoseStamped() #define the goal according to the features in PoseStamped
 xpos=input('\nEnter posx: ')
 ypos=input('\nEnter posy: ')
 #input the target (x,y) and assign it to the goal
 goal.pose.position.x=int(xpos)
 goal.pose.position.y=int(ypos)
 goal = assignment_2_2022.msg.PlanningGoal(goal)
 #send the new goal to the client server
 client.send_goal(goal)
 rospy.sleep(2)


 #return to the user interface
 user_select()

def cancel_sim():
 #client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
 client.cancel_goal()#send a signal to cancel the action of reaching the new target
 print("goal cancelled: going back to user select...")
 user_select() #send the new goal to the client server

def user_select():
 
 op=input("choose action: ")#enter the desired option
 

 if(op=="1"): #if set new target, go to new_position()
    new_position()
 elif(op=="2"):
    cancel_sim()#if cancel the target, go to cancel_sim()
#Main program
if __name__ == '__main__':
    try:
       #option for the user
        print("1: define position")
        print("2: cancel")
        rospy.init_node('nodeAclient')  # Initializes a rospy node
        
        client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)#create a client object for an Action client related to the message files Planning.action
        
        user_select()#enter to the main user interface
      
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
