"""


Initialize everything

current_state = 0 # 0 is for estop
prev_cmd = 0

while True:
    gui.update()
    state_controller.update()
    if state_controller.cmd == prev_cmd or none:
        arduino.pub(state_controller.cmd)

"""

from modules.guilib import GUIWindow
from modules.datalib import TurretCommand
from modules.statelib import StateController
from modules.seriallib import SerialConnection

if __name__ == "__main__":
    gui = GUIWindow()
    state_ctrl = StateController()
    arduino = SerialConnection(port='/dev/ttyACM0', baud=115200)

    while True:
        gui.update()
        state_ctrl.update(gui.isEStopped, gui.current_state)
        # print(state_ctrl.cmd)

        if state_ctrl.cmd != None:
            print(state_ctrl.cmd)
            arduino.publish(state_ctrl.cmd)

        # print(gui.isEStopped)
        # print(gui.current_state)
