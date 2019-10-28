import behaviorlib
from datalib import RobotCommand

class StateController:
    def __init__(self):
        self.state = 0
        self.cmd = None

        self._prev_cmd = RobotCommand()

    def update(self, isEStopped, current_state, target=None):
        if isEStopped:
            self.state = 0
        else:
            self.state = current_state

        if self.state == 0:
            self.cmd = behaviorlib.computeEstopCommand()
        elif self.state == 1:
            self.cmd = behaviorlib.computeForwardCommand()
        elif self.state == 2:
            self.cmd = behaviorlib.computeBackwardCommand()
        elif self.state == 3:
            self.cmd = behaviorlib.computeLeftCommand()
        elif self.state == 4:
            self.cmd = behaviorlib.computeRightCommand()
        elif self.state == 5:
            self.cmd = behaviorlib.computeShootCommand()
        elif self.state == 10:
            self.cmd = behaviorlib.computeState1Command(target)
        elif self.state == 11:
            self.cmd = behaviorlib.computeState2Command()

        if self.cmd == None:
            return

        # Don't send duplicate commands
        if self._prev_cmd == self.cmd:
            self.cmd = None
            return

        self._prev_cmd = self.cmd
