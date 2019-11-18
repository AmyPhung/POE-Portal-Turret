#!/usr/bin/env python

import rospy
from realsense_person.msg import PersonDetection
from portal_turret.msg import TwistLabeled
from std_msgs.msg import String
from portal_turret.msg import LabeledPointArray

import math

class PersonTracker:
    """
    Tracks 3D location of a specified person by name and face. Relies on being
    able to spot face at least once, then will keep track of the person as long
    as they remain in frame.
    """
    def __init__(self):
        rospy.init_node("PersonTracker")
        self.person_sub = rospy.Subscriber("/camera/person/detection_data",
                                           PersonDetection, self.personCB)
        self.target_sub = rospy.Subscriber("/target",
                                           String, self.targetCB)
        self.faces_sub = rospy.Subscriber("/detected_faces",
                                           LabeledPointArray, self.facesCB)
        self.twist_pub = rospy.Publisher("/state_controller/cmd_vel",
                                         TwistLabeled, queue_size=1)
        self.update_rate = rospy.Rate(10)

        self.dist_threshold = rospy.get_param("~dist_threshold", 30)
        print("Using dist_threshold = " + str(self.dist_threshold))
        self.linear_k = rospy.get_param("~linear_k", 0.7)
        print("Using linear_k = " + str(self.linear_k))
        self.angular_k = rospy.get_param("~angular_k", 0.3)
        print("Using angular_k = " + str(self.angular_k))

        self._person_msg = PersonDetection()
        self._target_msg = String()
        self._faces_msg = LabeledPointArray()
        self._twist_cmd = TwistLabeled()

        self._prev_ids = {} # Dictionary containing names and previous detection
                            # id values

    # Callback functions
    def personCB(self, msg):
        self._person_msg = msg

    def targetCB(self, msg):
        self._target_msg = msg

    def facesCB(self, msg):
        self._faces_msg = msg

    # Identify target within frame
    def findTargetIdx(self):
        """
        Find index of target in person detection data. Returns -1 if it can't
        find the target.
        """
        target = self._target_msg.data

        if target not in self._prev_ids:
            self._prev_ids[target] = [] # Add new list of id values
        else:
            prev_ids = self._prev_ids[target]

            # If target has already been identified with a prior id, then use
            # that info
            for idx in range(self._person_msg.detected_person_count):
                tracking_id = self._person_msg.persons[idx].person_id.tracking_id
                if tracking_id in prev_ids:
                    print("Found " + str(target))
                    print("Using id " + str(tracking_id))
                    return idx

        # If the code reaches this point, we can't rely on our dictionary. At
        # this point, we check to see if the person is even in the image. We do
        # this by computing the distance between the tracked target's face
        # and the tracked people to find the nearest person. If this distance
        # is below a certain threshold, we can safely assume they're the same
        # people and can add their ID to the dictionary

        for face in self._faces_msg.points:
            if face.label == target:
                idx, detection_id =  \
                    self.findNearestIdx((face.point.x, face.point.y),
                                        self._person_msg.persons,
                                        self.dist_threshold)
                if idx != -1: # If person is found, save detection id to dict
                    self._prev_ids[target].append(detection_id)
                return idx
        # If the code reaches this point, we can't find the target
        return -1

    def findNearestIdx(target_center, detected_people, threshold):
        """
        Finds index of detected person whose center is closest to the center
        of the identified target's face
        """
        # Threshold is max distance between the center of a face and an unknown
        # detected person to be considered the same person
        nearest_idx = -1
        detection_id = -1
        min_dist = 100000000000
        for i in range(len(detected_people)):
            person = detected_people[i]

            detected_cx = person.center_of_mass.image.x
            detected_cy = person.center_of_mass.image.y
            # TODO: Check coordinate system of each point + convert here

            distance = dist(detected_cx, detected_cy, \
                            target_center[0], target_center[1])

            if distance < threshold and distance < min_dist:
               nearest_idx = i
               detection_id = person.person_id

        return nearest_idx, detection_id

    # Control loop
    def computeTwistMessage(self, idx):
        # If no people are detected or there's no target, don't publish commands
        if len(self._person_msg.persons) == 0 or self._target_msg.data == "":
            self._twist_cmd = TwistLabeled()
            self._twist_cmd.label.data = 11
            return


        x = self._person_msg.persons[idx].center_of_mass.world.x
        z = self._person_msg.persons[idx].center_of_mass.world.z

        # Compute relative position - -100 for left of robot, 100 for right
        rel_pos = int(reMap(x,
                            0.5, -0.5,
                            100, -100))

        dist_pos = int(reMap(z,
                            2, 0,
                            100, 0))

        self._twist_cmd = TwistLabeled()
        self._twist_cmd.label.data = 10
        self._twist_cmd.twist.linear.x = dist_pos * self.linear_k # Multiply by proportional constant
        self._twist_cmd.twist.angular.z = rel_pos * self.angular_k # Multiply by proportional constant

    def run(self):
        while not rospy.is_shutdown():
            idx = self.findTargetIdx()
            if idx != -1: # Check for valid index value
                self.computeTwistMessage(idx)
                #rospy.loginfo("Linear Command: " + str(self._twist_cmd.twist.linear.x))
                #rospy.loginfo("Angular Command: " + str(self._twist_cmd.twist.angular.z))
                self.twist_pub.publish(self.twist_cmd)
            self.update_rate.sleep()

def dist(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

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
