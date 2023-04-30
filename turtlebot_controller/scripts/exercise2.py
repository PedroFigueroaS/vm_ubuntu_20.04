#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, TeleportAbsolute

pub = rospy.Publisher("my_turtle/cmd_vel", Twist)

def turtleCallback(msg):
	rospy.loginfo("Turtle subscriber @[%f, %f, %f]", msg.x, msg.y, msg.theta);
	vel = Twist()
	if (msg.x > 9.0):
	    vel.linear.x = 1.0
	    vel.angular.z = 1.0
	elif (msg.x < 1.5):
	    vel.linear.x = 1.0
	    vel.angular.z = -1.0
	else:
	    vel.linear.x = 1.0
	    vel.angular.z = 0.0

	pub.publish(vel)

def controller():
	rospy.init_node("controller")
	rospy.Subscriber("my_turtle/pose", Pose, turtleCallback)
	rospy.wait_for_service("/kill")
	client1 = rospy.ServiceProxy("/kill", Kill)
	client1("turtle1")
	rospy.wait_for_service("/spawn")
	client2 = rospy.ServiceProxy("/spawn", Spawn)
	client2(1.0, 5.0, 0.0, "my_turtle")
	rospy.wait_for_service("/my_turtle/teleport_absolute")
	client3 = rospy.ServiceProxy("/my_turtle/teleport_absolute", TeleportAbsolute)
	client3(1.5, 1.0 , 0.0)
	rospy.spin()

if __name__ == '__main__':
	controller()

