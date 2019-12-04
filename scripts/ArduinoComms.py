#!/usr/bin/env python

import rospy
import serial
import time
from geometry_msgs.msg import Twist
from portal_turret.msg import Shooter
from std_msgs.msg import Int16

class ArduinoComms:
    def __init__(self, port='/dev/ttyACM0', baud=115200):
        self.connection = serial.Serial(port, baud, timeout=.1)

        self.twist_cmd = Twist()
        self.shooter_cmd = Shooter()
        self.feed_cmd = Int16()

        rospy.init_node("ArduinoComms")
        self.twist_sub = rospy.Subscriber("/cmd_vel", Twist, self.twistCB)
        self.shooter_sub = rospy.Subscriber("/cmd_shoot", Shooter, self.shooterCB)
        self.feed_sub = rospy.Subscriber("/cmd_feed", Int16, self.feedCB)
        self.update_rate = rospy.Rate(10)

        self._max_send_rate = 30 # Hz
        self._last_msg_time = time.time()

    def twistCB(self, msg):
        self.twist_cmd = msg

    def shooterCB(self, msg):
        self.shooter_cmd = msg

    def feedCB(self, msg):
        self.feed_cmd = msg

    def sendCmds(self):
        # Prevent overloading the arduino with too many commands
        if (time.time() - self._last_msg_time < 1./self._max_send_rate):
            return

        self._last_msg_time = time.time()

        self.connection.write('c') # Tell arduino new cmd is coming
        self.connection.write('f')
        self.connection.write(str(int(self.twist_cmd.linear.x)))
        self.connection.write('a')
        self.connection.write(str(int(self.twist_cmd.angular.z)))
        self.connection.write('r')
        self.connection.write(str(int(self.shooter_cmd.r_cmd)))
        self.connection.write('l')
        self.connection.write(str(int(self.shooter_cmd.l_cmd)))
        self.connection.write('d')
        self.connection.write(str(int(self.feed_cmd.data)))
        self.connection.write('e') # Tell arduino end of cmd

    def run(self):
        while not rospy.is_shutdown():
            # if self.twist_cmd == None:
            #     rospy.loginfo('MSG: No twist data published')
            #     self.update_rate.sleep()
            #     continue
            # if self.shooter_cmd == None:
            #     rospy.loginfo('MSG: No shooter data published')
            #     self.update_rate.sleep()
            #     continue
            self.sendCmds()
            self.update_rate.sleep()

if __name__ == "__main__":
    arduino_comms = ArduinoComms()
    arduino_comms.run()
