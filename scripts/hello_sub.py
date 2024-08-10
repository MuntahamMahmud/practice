#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from muntaham_pkg.msg import hello_msg

def clbk(self):
    rospy.loginfo(f"{self.num} {self.tname}")

if __name__=="__main__":
    rospy.init_node("cute_subscriber",anonymous=True)
    sub=rospy.Subscriber("chatting",hello_msg,clbk)
    rospy.spin()