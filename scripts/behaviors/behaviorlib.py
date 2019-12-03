from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from portal_turret.msg import Shooter

# Estop behavior
def computeEstopCommand():
    twist_cmd = Twist()
    shooter_cmd = Shooter()
    feed_cmd = Int16()

    twist_cmd.linear.x = 0
    twist_cmd.angular.z = 0
    shooter_cmd.r_cmd = 0
    shooter_cmd.l_cmd = 0
    feed_cmd.data = 0
    return twist_cmd, shooter_cmd, feed_cmd

# Teleop behaviors
def computeForwardCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value
    feed_cmd = None
    twist_cmd.linear.x = 40
    twist_cmd.angular.z = 0
    return twist_cmd, shooter_cmd, feed_cmd

def computeBackwardCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value
    feed_cmd = None
    twist_cmd.linear.x = -40
    twist_cmd.angular.z = 0
    return twist_cmd, shooter_cmd, feed_cmd

def computeLeftCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value
    feed_cmd = None
    twist_cmd.linear.x = 0
    twist_cmd.angular.z = 40
    return twist_cmd, shooter_cmd, feed_cmd

def computeRightCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value
    feed_cmd = None
    twist_cmd.linear.x = 0
    twist_cmd.angular.z = -40
    return twist_cmd, shooter_cmd, feed_cmd

def computeShootOnCommand():
    twist_cmd = None # Will retain previous value
    shooter_cmd = Shooter()
    feed_cmd = None
    shooter_cmd.r_cmd = 50
    shooter_cmd.l_cmd = 50
    return twist_cmd, shooter_cmd, feed_cmd

def computeShootOffCommand():
    twist_cmd = None # Will retain previous value
    shooter_cmd = Shooter()
    feed_cmd = None
    shooter_cmd.r_cmd = 0
    shooter_cmd.l_cmd = 0
    return twist_cmd, shooter_cmd, feed_cmd

def computeFeedOnCommand():
    twist_cmd = None # Will retain previous value
    shooter_cmd = None
    feed_cmd = Int16()
    feed_cmd.data = 100
    return twist_cmd, shooter_cmd, feed_cmd
def computeFeedOffCommand():
    twist_cmd = None # Will retain previous value
    shooter_cmd = None
    feed_cmd = Int16()
    feed_cmd.data = 0
    return twist_cmd, shooter_cmd, feed_cmd

# High level behaviors
def computeState1Command(sc_twist_cmd):
    # Follows people in frame - nobody in particular
    twist_cmd = sc_twist_cmd
    shooter_cmd = None
    feed_cmd = None
    return twist_cmd, shooter_cmd, feed_cmd

def computeState2Command(sc_twist_cmd):
    # Follows a specified target
    twist_cmd = sc_twist_cmd
    shooter_cmd = None
    feed_cmd = None
    return twist_cmd, shooter_cmd, feed_cmd

def computeTeleopCommand(joy_cmd):
    # axis 1: foward (1), backward (-1)
    # axis 0: left (1), right (-1)
    # axis 5: right trigger (1 unpressed, -1 pressed)
    # button 5: right bumper (0 unpressed, 1 pressed)

    # Right joystick used for driving
    twist_cmd = Twist()
    shooter_cmd = Shooter()
    feed_cmd = Int16()

    # Wait for joystick
    if len(joy_cmd.axes) == 0:
        return twist_cmd, shooter_cmd, feed_cmd

    twist_cmd.linear.x = int(joy_cmd.axes[1] * 100)
    twist_cmd.angular.z = int(joy_cmd.axes[0] * 100)

    shooter_cmd.r_cmd = int(reMap(joy_cmd.axes[5], -1, 1, 100, 0))
    shooter_cmd.l_cmd = int(reMap(joy_cmd.axes[5], -1, 1, 100, 0))

    feed_cmd.data = 100*joy_cmd.buttons[5]

    return twist_cmd, shooter_cmd, feed_cmd

def reMap(value, maxInput, minInput, maxOutput, minOutput):
	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput
	scaled_value = float(value - minInput) / float(inputSpan)
	return minOutput + (scaled_value * outputSpan)
