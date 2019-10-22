"""
Contains code for a SerialConnection object to connect to the Arduino
"""

import serial
import keyboard

class SerialConnection:
    """
    Sets up a serial connection with an Arduino

    Args:
        port (str): String containing Arduino port. Defaults to '/dev/ttyACM0'
        baud (int): Baud rate for connection. Defaults to 115200
    Attributes:
    """
    def __init__(self, port='/dev/ttyACM0', baud=115200):
        self.arduino = serial.Serial(port, baud, timeout=.1)

    def publish(self, cmd):
        self.arduino.write('c') # Tell arduino new cmd is coming
        self.arduino.write('f')
        self.arduino.write(str(int(cmd.f_vel)))
        self.arduino.write('a')
        self.arduino.write(str(int(cmd.a_vel)))
        self.arduino.write('r')
        self.arduino.write(str(int(cmd.r_turret)))
        self.arduino.write('l')
        self.arduino.write(str(int(cmd.l_turret)))
        self.arduino.write('e') # Tell arduino end of cmd
