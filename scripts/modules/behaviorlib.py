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
    cmd.a_vel = 40
    return cmd
def computeRightCommand():
    cmd = RobotCommand()
    cmd.f_vel = 0
    cmd.a_vel = -40
    return cmd
def computeShootCommand():
    cmd = RobotCommand()
    cmd.r_turret = 100
    cmd.l_turret = 100
    return cmd

# High level behaviors
def computeState1Command(target):
    cmd = RobotCommand()
    cmd.f_vel = 40
    cmd.a_vel = target[0]
    return cmd

def computeState2Command():
    return None
