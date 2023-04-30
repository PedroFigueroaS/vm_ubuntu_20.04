#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <my_actions/FibonacciAction.h>

int main (int argc, char **argv)
{
	
  ros::init(argc, argv, "test_fibonacci");

  // create the action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<my_actions::FibonacciAction> ac("fibonacci", true);

  ROS_INFO("Waiting for action server to start.");
  // wait for the action server to start
  ac.waitForServer(); //will wait for infinite time

  ROS_INFO("Action server started, sending goal.");
  // send a goal to the action
  my_actions::FibonacciGoal goal;
  goal.order = 20;
  ac.sendGoal(goal);

  //wait for the action to return
  bool finished_before_timeout = ac.waitForResult(ros::Duration(30.0));

  if (finished_before_timeout)
  {
    actionlib::SimpleClientGoalState state = ac.getState();
    ROS_INFO("Action finished: %s",state.toString().c_str());
    my_actions::FibonacciResultConstPtr seq= ac.getResult();
    for (int i = 0; i < goal.order; i++){
		std::cout << seq->sequence[i] << " ";
	}
	std::cout << std::endl;
    
  }
  else{
    ROS_INFO("Action did not finish before the time out.");
    ac.cancelGoal(); 
    ROS_INFO("Goal has been cancelled");
   }


  //exit
  return 0;
}
