from geometry_msgs.msg import Twist
from portal_turret.msg import Shooter

# Estop behavior
def computeEstopCommand():
    twist_cmd = Twist()
    shooter_cmd = Shooter()

    twist_cmd.linear.x = 0
    twist_cmd.angular.z = 0
    shooter_cmd.r_cmd = 0
    shooter_cmd.l_cmd = 0
    return twist_cmd, shooter_cmd

# Teleop behaviors
def computeForwardCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value

    twist_cmd.linear.x = 40
    twist_cmd.angular.z = 0
    return twist_cmd, shooter_cmd

def computeBackwardCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value

    twist_cmd.linear.x = -40
    twist_cmd.angular.z = 0
    return twist_cmd, shooter_cmd

def computeLeftCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value

    twist_cmd.linear.x = 0
    twist_cmd.angular.z = 40
    return twist_cmd, shooter_cmd

def computeRightCommand():
    twist_cmd = Twist()
    shooter_cmd = None # Will retain previous value

    twist_cmd.linear.x = 0
    twist_cmd.angular.z = -40
    return twist_cmd, shooter_cmd

def computeShootOnCommand():
    twist_cmd = None # Will retain previous value
    shooter_cmd = Shooter()
    shooter_cmd.r_cmd = 100
    shooter_cmd.l_cmd = 100
    return twist_cmd, shooter_cmd

def computeShootOffCommand():
    twist_cmd = None # Will retain previous value
    shooter_cmd = Shooter()
    shooter_cmd.r_cmd = 0
    shooter_cmd.l_cmd = 0
    return twist_cmd, shooter_cmd

# High level behaviors TODO
def computeState1Command(target):
    # if target == None:
    #     return None
    # cmd = RobotCommand()
    # cmd.f_vel = 40
    # cmd.a_vel = -target[0]
    return None, None

def computeState2Command():
    return None, None
