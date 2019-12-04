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

        self._max_send_rate = 10 # Hz (keep below 60)
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
        # Encode command in string to send to arduino
        ser_cmd = "f" + str(int(self.twist_cmd.linear.x)) + \
                  "a" + str(int(self.twist_cmd.angular.z)) + \
                  "r" + str(int(self.shooter_cmd.r_cmd)) + \
                  "l" + str(int(self.shooter_cmd.l_cmd)) + \
                  "d" + str(int(self.feed_cmd.data)) + \
                  "e"

        # Send string command
        self.connection.write(ser_cmd)
        # time.sleep(0.1)

        print("Lap-bot: ---------------------------------")
        print("Current time: " + str(time.time()))
        print("Sending: " + ser_cmd)

    def run(self):
        while not rospy.is_shutdown():
            self.sendCmds()

            # For Debugging - prints out arduino output
            # print(self.connection.in_waiting)
            msg = ""
            while self.connection.in_waiting > 0:
                msg = msg + self.connection.readline()

            print("Arduino: ---------------------------------")
            print(str(msg))

            self.update_rate.sleep()

if __name__ == "__main__":
    arduino_comms = ArduinoComms()
    arduino_comms.run()
