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
from modules.statelib import StateController
from modules.seriallib import SerialConnection
from modules.cvlib import TrackingSystem


if __name__ == "__main__":
    arduino_avail = True

    gui = GUIWindow()
    state_ctrl = StateController()
    try:
        arduino = SerialConnection(port='/dev/ttyACM0', baud=115200)
    except:
        arduino_avail = False
        print "No Arduino Found. Running GUI only"
    cv = TrackingSystem(gui=True)

    while True:
        gui.update()
        target = cv.update()
        state_ctrl.update(gui.isEStopped, gui.current_state, target)

        if state_ctrl.cmd != None:
            print state_ctrl.cmd
            if arduino_avail:
                arduino.publish(state_ctrl.cmd)
