#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

#######################
# YOUR FUNCTIONS HERE #
#######################
def forward(speed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = speed
      vel_msg.linear.y = 0 
      vel_msg.angular.z = 0 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1) 
def right(speed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = 0
      vel_msg.linear.y = speed 
      vel_msg.angular.z = 0 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1)
def left(speed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = 0
      vel_msg.linear.y = speed 
      vel_msg.angular.z = 0 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1)
def back(speed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = speed
      vel_msg.linear.y = 0 
      vel_msg.angular.z = 0 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1)
def around(speed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = 0
      vel_msg.linear.y = 0 
      vel_msg.angular.z = speed 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1)
def aroundleft(xspeed,zspeed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = xspeed
      vel_msg.linear.y = 0 
      vel_msg.angular.z = zspeed 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1)
def aroundright(xspeed,zspeed,duration):
    for i in range(0,duration):
      vel_msg.linear.x = xspeed
      vel_msg.linear.y = 0 
      vel_msg.angular.z = zspeed 
      velocity_publisher.publish(vel_msg)
      rospy.sleep(0.1)







###########################
# YOUR FUNCTIONS HERE END #
###########################


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################
        forward(0.4,30)
        right(0.4,30)
        left(-0.3,30)
        back (-0.4,30)
        around(0.8,30) 
        aroundleft(-0.3,-0.3,100)
        aroundright(0.3,-0.3,100)
        
        
 
        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
