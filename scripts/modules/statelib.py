import behaviorlib
from datalib import TurretCommand

class StateController:
    def __init__(self):
        self.state = 0
        self.cmd = None

        self._prev_cmd = TurretCommand()

    def update(self, isEStopped, current_state):
        if isEStopped:
            self.state = 0
        else:
            self.state = current_state

        if self.state == 0:
            self.cmd = behaviorlib.computeEstopCommand()
        elif self.state == 1:
            self.cmd = behaviorlib.computeTeleopCommand()
        elif self.state == 2:
            self.cmd = behaviorlib.computeState2Command()

        if self.cmd == None:
            return

        # Don't send duplicate commands
        if self._prev_cmd == self.cmd:
            self.cmd = None
            return

        self._prev_cmd = self.cmd
