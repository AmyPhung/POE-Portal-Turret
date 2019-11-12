#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from portal_turret.msg import Shooter

import behaviors.behaviorlib as behaviorlib

class StateController:
    def __init__(self):
        self.state = 0
        self.estop = True

        rospy.init_node("StateController")
        self.state_sub = rospy.Subscriber("/state", Int16, self.stateCB)
        self.estop_sub = rospy.Subscriber("/estop", Bool, self.estopCB)
        self.sc_twist_sub = rospy.Subscriber("state_controller/cmd_vel",
                                         TwistLabeled, self.sc_twistCB)

        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.shooter_pub = rospy.Publisher("/cmd_shoot", Shooter, queue_size=1)
        self.feed_pub = rospy.Publisher("/cmd_feed", Int16, queue_size=1)
        self.update_rate = rospy.Rate(10)

        self._prev_twist_cmd = Twist()
        self._prev_shooter_cmd = Shooter()
        self._prev_feed_cmd = Int16()

        self._sc_twist_cmd = Twist()

    def stateCB(self, msg):
        self.state = msg.data

    def estopCB(self, msg):
        self.estop = msg.data

    def sc_twistCB(self, msg):
        if sc_twist_sub.label == self.state:
            self._sc_twist_cmd = msg.twist

    def run(self):
        while not rospy.is_shutdown():
            if self.state == 0 or self.estop:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeEstopCommand()
            elif self.state == 1:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeForwardCommand()
            elif self.state == 2:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeBackwardCommand()
            elif self.state == 3:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeLeftCommand()
            elif self.state == 4:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeRightCommand()
            elif self.state == 5:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeShootOnCommand()
            elif self.state == 6:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeShootOffCommand()
            elif self.state == 7:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeFeedOnCommand()
            elif self.state == 8:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeFeedOffCommand()
            elif self.state == 10:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeState1Command(self._sc_twist_cmd)
            elif self.state == 11:
                twist_cmd, shooter_cmd, feed_cmd = behaviorlib.computeState2Command()

            # Don't send invalid or duplicate command
            if twist_cmd != None and \
               twistIsUnique(twist_cmd, self._prev_twist_cmd):
               self.twist_pub.publish(twist_cmd)
               self._prev_twist_cmd = twist_cmd
            if shooter_cmd != None and \
               shooterIsUnique(shooter_cmd, self._prev_shooter_cmd):
               self.shooter_pub.publish(shooter_cmd)
               self._prev_shooter_cmd = shooter_cmd
            if feed_cmd != None and \
               feedIsUnique(feed_cmd, self._prev_feed_cmd):
               self.feed_pub.publish(feed_cmd)
               self._prev_feed_cmd = feed_cmd

            self.update_rate.sleep()

def twistIsUnique(twist1, twist2):
    if twist1.linear.x == twist2.linear.x and \
       twist1.linear.y == twist2.linear.y and \
       twist1.linear.z == twist2.linear.z and \
       twist1.angular.x == twist2.angular.x and \
       twist1.angular.y == twist2.angular.y and \
       twist1.angular.z == twist2.angular.z:
       return False
    else:
       return True

def shooterIsUnique(shooter1, shooter2):
    if shooter1.r_cmd == shooter2.r_cmd and \
       shooter1.l_cmd == shooter2.l_cmd:
       return False
    else:
       return True

def feedIsUnique(feed1, feed2):
    if feed1.data == feed2.data:
        return False
    else:
        return True


if __name__ == "__main__":
    sc = StateController()
    sc.run()
