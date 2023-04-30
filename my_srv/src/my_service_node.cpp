#include "ros/ros.h"
#include "my_srv/Velocity.h"
#include <stdlib.h>
#include <stdio.h>

bool my_random(my_srv::Velocity::Request &req, my_srv::Velocity::Response &res){
	res.x = req.min + (rand()/(RAND_MAX/(req.max-req.min)));
	res.z = req.min + (rand()/(RAND_MAX/(req.max-req.min)));
	return true;
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "velocity_server");
	ros::NodeHandle n;
	ros::ServiceServer service= n.advertiseService("/velocity", my_random);
	ros::spin();
	return 0;
}
