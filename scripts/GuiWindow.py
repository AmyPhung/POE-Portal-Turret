#!/usr/bin/env python
"""
Current state:


Estop
Teleop
Mission


switchState()

Flow:
need to e-stop before switching states
Each state has an update function that modifies it's current command

In main

"""


import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

import Tkinter as tk

class GUIWindow:
    def __init__(self):
        rospy.init_node("GuiWindow")
        self.state_pub = rospy.Publisher("/state", Int16, queue_size=1)
        self.estop_pub = rospy.Publisher("/estop", Bool, queue_size=1)
        self.update_rate = rospy.Rate(10)

        # GUI Setup
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.isEStopped = True
        self.current_state = 1

        self.button_estop = tk.Button(self.root, width=3, text="START",
                bg = "green", command = self.estopCB)
        self.button_estop.pack()

        # Teleop
        self.frame_teleop = tk.Frame(width=200, height=200, #bg="gray",
                                     colormap="new")
        self.frame_teleop.pack()
        self.button_w = tk.Button(self.frame_teleop, #width=20, height=20,
                text="Forwards",
                command = self.wCB)
        self.button_w.grid(row=0,column=1)
        self.root.bind('w', self.wCB)

        self.button_s = tk.Button(self.frame_teleop, #width=20, height=20,
                text="Backwards",
                command = self.sCB)
        self.button_s.grid(row=2,column=1)
        self.root.bind('s', self.sCB)

        self.button_a = tk.Button(self.frame_teleop, #width=20, height=20,
                text="Left",
                command = self.aCB)
        self.button_a.grid(row=1,column=0)
        self.root.bind('a', self.aCB)

        self.button_d = tk.Button(self.frame_teleop, #width=20, height=20,
                text="Right",
                command = self.dCB)
        self.button_d.grid(row=1,column=2)
        self.root.bind('d', self.dCB)

        self.button_stop = tk.Button(self.frame_teleop, #width=20, height=20,
                text="Stop",
                command = self.stopCB)
        self.button_stop.grid(row=1,column=1)
        self.root.bind('q', self.stopCB)

        self.button_shooterOn = tk.Button(self.root, width=15,
                text="Shooter On",
                command = self.shootOnCB)
        self.button_shooterOn.pack()

        self.button_shooterOff = tk.Button(self.root, width=15,
                text="Shooter Off",
                command = self.shootOffCB)
        self.button_shooterOff.pack()

        self.button_feedOn = tk.Button(self.root, width=15,
                text="Feed On",
                command = self.feedOnCB)
        self.button_feedOn.pack()

        self.button_feedOff = tk.Button(self.root, width=15,
                text="Shooter Off",
                command = self.feedOffCB)
        self.button_feedOff.pack()

        # State 1
        self.button_state1 = tk.Button(self.root, width=30,
                text="Switch to state1",
                command = self.state1CB)
        self.button_state1.pack()

        # State 2
        self.button_state2 = tk.Button(self.root, width=30,
                text="Switch to state 2",
                command = self.state2CB)
        self.button_state2.pack()

        # Output Window
        self.label_output1 = tk.Label(self.root, text="Disactivated",
                width = 30, height = 1, fg="white", bg="black")
        self.label_output1.pack()
        self.label_output2 = tk.Label(self.root, text="Mode: teleop",
                width = 30, height = 1, fg="white", bg="black")
        self.label_output2.pack()

        # Save previous values to avoid publishing duplicates
        self._prev_state = 0
        self._prev_isEStopped = False

    def estopCB(self):
        if self.isEStopped == True:
            self.label_output1.configure(text = "Activated")
            self.isEStopped = False
            self.button_estop.configure(text = "E-STOP", bg = "red")
        else:
            self.label_output1.configure(text = "Disactivated")
            self.isEStopped = True
            self.button_estop.configure(text = "START", bg = "green")

    def stopCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - stopped")
        self.current_state = 0
    def wCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - W")
        self.current_state = 1
    def sCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - S")
        self.current_state = 2
    def aCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - A")
        self.current_state = 3
    def dCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - D")
        self.current_state = 4

    def shootOnCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - shoot on")
        self.current_state = 5

    def shootOffCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - shoot off")
        self.current_state = 6

    def feedOnCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - feed on")
        self.current_state = 7

    def feedOffCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - feed off")
        self.current_state = 8

    # Note: Reserving 6-9 for other low-level behaviors

    def state1CB(self):
        self.label_output2.configure(text = "Mode: state1")
        self.current_state = 10

    def state2CB(self):
        self.label_output2.configure(text = "Mode: state2")
        self.current_state = 11

    def run(self):
        while not rospy.is_shutdown():
            self.root.update()

            # Don't send duplicates
            if self.current_state != self._prev_state:
                state_msg = Int16()
                state_msg.data = self.current_state
                self.state_pub.publish(state_msg)
                self._prev_state = self.current_state
            if self.isEStopped != self._prev_isEStopped:
                estop_msg = Bool()
                estop_msg.data = self.isEStopped
                self.estop_pub.publish(estop_msg)
                self._prev_isEStopped = self.isEStopped

if __name__ == "__main__":
    w = GUIWindow()
    w.run()
