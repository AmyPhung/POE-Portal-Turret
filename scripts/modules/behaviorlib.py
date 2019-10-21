from datalib import TurretCommand
import keyboard

def computeEstopCommand():
    # print("here0")
    cmd = TurretCommand()
    cmd.f_vel = 0
    cmd.a_vel = 0
    return cmd

def computeTeleopCommand():
    # print("here1")
    cmd = TurretCommand()
    if keyboard.is_pressed(' '):
        cmd.f_vel = 0
        cmd.a_vel = 0
    elif keyboard.is_pressed('w'):
        cmd.f_vel = 40
        cmd.a_vel = 0
    elif keyboard.is_pressed('a'):
        cmd.f_vel = 0
        cmd.a_vel = 20
    elif keyboard.is_pressed('s'):
        cmd.f_vel = -40
        cmd.a_vel = 0
    elif keyboard.is_pressed('d'):
        cmd.f_vel = 0
        cmd.a_vel = -20
    else:
        return None
    return cmd

def computeState2Command():
    # print("here2")
    return None
