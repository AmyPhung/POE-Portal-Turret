#!/usr/bin/env python

import rospy
from realsense_person.msg import PersonDetection
from portal_turret.msg import TwistLabeled

class Tracker:
    def __init__(self):
        self.person_sub = rospy.Subscriber("/camera/person/detection_data",
                                           PersonDetection, self.personCB)
        self.twist_pub = rospy.Publisher("state_controller/cmd_vel",
                                         TwistLabeled, queue_size=1)
        self.update_rate = rospy.Rate(10)

        self.person_msg = PersonDetection()
        self.twist_cmd = TwistLabeled()



    def personCB(self, msg):
        self.person_msg = msg

    def run(self):
        while not rospy.is_shutdown():
            self.computeTwistMessage()
            self.twist_pub.publish(self.twist_cmd)
            self.update_rate.sleep()

    def computeTwistMessage(self):
        x = self.person_msg.persons.center_of_mass.world.x
        z = self.person_msg.persons.center_of_mass.world.z

        # Compute relative position - -100 for left of robot, 100 for right
        rel_pos = int(reMap(x,
                            0.5, -0.5,
                            100, -100))

        dist_pos = int(reMap(z,
                            2, 0,
                            100, 0))

        self.twist_cmd = TwistLabeled()
        self.twist_cmd.linear.x = dist_pos * 0.5 # Multiply by proportional constant
        self.twist_cmd.angular.z = rel_pos * 0.5 # Multiply by proportional constant

def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaled_value = float(value - minInput) / float(inputSpan)

	return minOutput + (scaled_value * outputSpan)
