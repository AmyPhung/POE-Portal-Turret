#!/usr/bin/env python

import rospy
from realsense_person.msg import PersonDetection
from portal_turret.msg import TwistLabeled
from std_msgs.msg import String
from portal_turret.msg import LabeledPointArray

class PersonTracker:
    def __init__(self):
        rospy.init_node("PersonTracker")
        self.person_sub = rospy.Subscriber("/camera/person/detection_data",
                                           PersonDetection, self.personCB)
        self.target_sub = rospy.Subscriber("/target",
                                           String, self.targetCB)
        self.faces_sub = rospy.Subscriber("/detected_faces",
                                           LabeledPointArray, self.facesCB)
        self.twist_pub = rospy.Publisher("state_controller/cmd_vel",
                                         TwistLabeled, queue_size=1)
        self.update_rate = rospy.Rate(10)

        self._person_msg = PersonDetection()
        self._target_msg = String()
        self._faces_msg = LabeledPointArray()
        self._twist_cmd = TwistLabeled()

    # Callback functions
    def personCB(self, msg):
        self._person_msg = msg

    def targetCB(self, msg):
        self._target_msg = msg

    def facesCB(self, msg):
        self._faces_msg = msg

    # Identify target within frame
    def findTargetIdx(self):
        # TODO:
        """
        self.prev_ids = {}

        if 

        distance threshold # distance for person to still match

        if target in detected_faces:
            self.findNearestIdx(detected_faces[target].image_center,
                                self._person_msg.persons)

            if dist(detected_faces.image_center,

        center of mass.image

    def findNearestIdx(target_center, detected_people, threshold):
        # threshold is max distance for it to be considered the same person
        nearest_idx = -1
        min_dist = 100000000000
        for i in range(len(detected_people)):
            person = detected_people[i]

            detected_center = (person.center_of_mass.image.x,
                               person.center_of_mass.image.y)

            if dist(detected_center, target_center) < min_dist and  \
               dist(detected_center, target_center) < threshold:
               nearest_idx = i

       return nearest_idx


        """
        # self._person_msg.persons[0].center_of_mass.world.x

    # Control loop
    def computeTwistMessage(self):
        # If no people are detected or there's no target, don't publish commands
        if len(self._person_msg.persons) == 0 or self._target_msg.data == "":
            self._twist_cmd = TwistLabeled()
            self._twist_cmd.label.data = 10
            return


        x = self._person_msg.persons[0].center_of_mass.world.x
        z = self._person_msg.persons[0].center_of_mass.world.z

        # Compute relative position - -100 for left of robot, 100 for right
        rel_pos = int(reMap(x,
                            0.5, -0.5,
                            100, -100))

        dist_pos = int(reMap(z,
                            2, 0,
                            100, 0))

        self._twist_cmd = TwistLabeled()
        self._twist_cmd.label.data = 10
        self._twist_cmd.twist.linear.x = dist_pos * 0.5 # Multiply by proportional constant
        self._twist_cmd.twist.angular.z = rel_pos * 0.5 # Multiply by proportional constant

    def run(self):
        while not rospy.is_shutdown():
            self.computeTwistMessage()
            #rospy.loginfo("Linear Command: " + str(self._twist_cmd.twist.linear.x))
            #rospy.loginfo("Angular Command: " + str(self._twist_cmd.twist.angular.z))
            self.twist_pub.publish(self.twist_cmd)
            self.update_rate.sleep()

def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaled_value = float(value - minInput) / float(inputSpan)

	return minOutput + (scaled_value * outputSpan)

if __name__ == "__main__":
    person_tracker = PersonTracker()
    person_tracker.run()
