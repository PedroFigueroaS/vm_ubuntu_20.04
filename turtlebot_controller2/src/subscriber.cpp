#include "ros/ros.h"
#include "turtlesim/Pose.h"
#include "geometry_msgs/Twist.h"

void turtleCallback(const turtlesim::Pose::ConstPtr &msg)
{
    ROS_INFO("Turtle subscriber@[%f,%f, %f]",
             msg->x, msg->y, msg->theta);
}

int main(int argc, char **argv)
{
    ros::Publisher pub;
    // Initializethe node,setup the NodeHandle for handling the communication with the ROS
    // system
    ros::init(argc, argv, "turtlebot_subscriber");
    ros::NodeHandle nh;
    // Define the subscriber to turtle's posi@on
    ros::Subscriber sub = nh.subscribe("turtle1/pose", 1, turtleCallback);
    pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1);
    while (1)
    {
        geometry_msgs::Twist my_vel;
        my_vel.linear.x = 1.0;
        my_vel.angular.z = 1.0;
        pub.publish(my_vel);
        ros::spinOnce();
    }

    // ros::spin();
    return 0;
}
