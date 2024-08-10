#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from muntaham_pkg.msg import hello_msg

if __name__=="__main__":
    rospy.init_node("cute_publisher",anonymous=True)
    pub=rospy.Publisher("chatting",hello_msg,queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        m=hello_msg()
        m.num= 45
        m.tname= "muntaham"
        
        pub.publish(m)
        rate.sleep()