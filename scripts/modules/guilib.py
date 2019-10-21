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

        self.button_shooter = tk.Button(self.root, width=15,
                text="Test Shooter",
                command = self.shootCB)
        self.button_shooter.pack()

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

    def shootCB(self, event=None):
        self.label_output2.configure(text = "Mode: teleop - shoot")
        self.current_state = 5

    # Note: Reserving 6-9 for other low-level behaviors

    def state1CB(self):
        self.label_output2.configure(text = "Mode: state1")
        self.current_state = 10

    def state2CB(self):
        self.label_output2.configure(text = "Mode: state2")
        self.current_state = 11

    def update(self):
        self.root.update()


if __name__ == "__main__":
    w = GUIWindow()

    while True:
        w.update()
