#include "ros/ros.h"
#include "turtlesim/Pose.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Spawn.h"
#include "turtlebot_controller/Vel.h"
#include "my_srv/Velocity.h"

void turtleCallback(const turtlesim::Pose::ConstPtr& msg)
{
ROS_INFO("Turtle subscriber@[%f, %f, %f]",
msg->x, msg->y, msg->theta);
}

int main (int argc, char **argv)
{
	ros::init(argc, argv, "turtlebot_subscriber");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe("my_new_turtle/pose", 1,turtleCallback); 
	ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("my_new_turtle/cmd_vel", 1);
	ros::Publisher pub2 = nh.advertise<turtlebot_controller::Vel>("/my_vel",1);
	ros::ServiceClient client = nh.serviceClient<turtlesim::Spawn>("/spawn");
	ros::ServiceClient client2 = nh.serviceClient<my_srv::Velocity>("/velocity");
	
	turtlesim::Spawn spawn;
	spawn.request.x = 1.0;
	spawn.request.y = 1.0;
	spawn.request.theta = 0.0;
	spawn.request.name = "my_new_turtle";
	
	client.call(spawn);
	
	ros::Rate rate(1);
	my_srv::Velocity server_vel;
	while (ros::ok()){
		server_vel.request.min = 0.0;
		server_vel.request.max = 5.0;
		client2.call(server_vel);
	
		geometry_msgs::Twist my_vel;
		my_vel.linear.x = server_vel.response.x;
		my_vel.angular.z = server_vel.response.z;
		pub.publish(my_vel);
		turtlebot_controller::Vel new_vel;
		new_vel.name = "linear";
		new_vel.vel = my_vel.linear.x;
		pub2.publish(new_vel);
		ros::spinOnce();
		rate.sleep();
	}
	return 0;
}

