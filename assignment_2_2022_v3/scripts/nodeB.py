#! /usr/bin/env python3

import rospy

import time
from std_srvs.srv import Empty, EmptyResponse
import assignment_2_2022.msg

ncancelled=0
nreached=0

def serv_callback(req):#service function
    global ncancelled , nreached
    print("number of targets cancelled: \n",ncancelled)
    print("number of targets reached: \n",nreached)
   #print the number of times the goal is reached and cancelled 
    return EmptyResponse()


def cllback(msg):#subscriber function
 global ncancelled 
 global nreached
 if (msg.status.status==2):#each time a goal es cancelled, 
    
    ncancelled=ncancelled+1
 elif (msg.status.status==3):
    
    nreached=nreached+1

#main function
if __name__ == '__main__':
        # Initializes a rospy node
 rospy.init_node('nodeB')
 rospy.Subscriber("/reaching_goal/result",assignment_2_2022.msg.PlanningActionResult,cllback)#subsrcibe to the topic /reaching_goal and call the cllback function
 rospy.Service("reach_cancel_ints",Empty,serv_callback)#call the service "reach_cancel_ints" and call the serv_callback() function
 rospy.spin()#keep the program working until python terminates it
