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
import tkinter as tk

class GUIWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.isEStopped = True
        self.current_state = 1

        self.button_estop = tk.Button(self.root, width=3, text="START",
                bg = "green", command = self.estopCB)
        self.button_estop.pack()

        # State 1
        self.button_teleop = tk.Button(self.root, width=30,
                text="Switch to teleoperated state",
                command = self.teleopCB)
        self.button_teleop.pack()

        # State 2
        self.button_state2 = tk.Button(self.root, width=30,
                text="Switch to state 2",
                command = self.state2CB)
        self.button_state2.pack()

        self.label_output1 = tk.Label(self.root, text="Disactivated",
                width = 30, height = 1, fg="white", bg="black")
        self.label_output1.pack()
        self.label_output2 = tk.Label(self.root, text="Mode: teleop",
                width = 30, height = 1, fg="white", bg="black")
        self.label_output2.pack()



    def estopCB(self):
        if self.isEStopped == True:
            self.label_output1.configure(text = "Activated")
            self.isEStopped = False
            self.button_estop.configure(text = "E-STOP", bg = "red")
        else:
            self.label_output1.configure(text = "Disactivated")
            self.isEStopped = True
            self.button_estop.configure(text = "START", bg = "green")

    def teleopCB(self):
        self.label_output2.configure(text = "Mode: teleop")
        self.current_state = 1

    def state2CB(self):
        self.label_output2.configure(text = "Mode: state2")
        self.current_state = 2

    def update(self):
        self.root.update()

if __name__ == "__main__":
    w = GUIWindow()

    while True:
        w.update()
