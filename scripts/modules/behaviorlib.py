from datalib import RobotCommand

def computeEstopCommand():
    cmd = RobotCommand()
    cmd.f_vel = 0
    cmd.a_vel = 0
    return cmd

# Teleop behaviors
def computeForwardCommand():
    cmd = RobotCommand()
    cmd.f_vel = 40
    cmd.a_vel = 0
    return cmd
def computeBackwardCommand():
    cmd = RobotCommand()
    cmd.f_vel = -40
    cmd.a_vel = 0
    return cmd
def computeLeftCommand():
    cmd = RobotCommand()
    cmd.f_vel = 0
    cmd.a_vel = 20
    return cmd
def computeRightCommand():
    cmd = RobotCommand()
    cmd.f_vel = 0
    cmd.a_vel = -20
    return cmd
def computeShootCommand():
    cmd = RobotCommand()
    cmd.r_turret = 100
    cmd.l_turret = 100
    return cmd

# High level behaviors
def computeState1Command():
    return None

def computeState2Command():
    return None
