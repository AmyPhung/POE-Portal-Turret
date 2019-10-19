# # Symbolic link to Arduino installation directory - see below
# ARDUINO_DIR   = C:/Arduino
# ARDMK_DIR     = ../../../Arduino-Makefile/Arduino.mk # Make sure it's in the same directory
# MONITOR_PORT  = com3
# ARCHITECTURE  = avr
# BOARD_TAG     = mega2560
# MONITOR_CMD   = putty
# MONITOR_PARAMS = 8,1,n,N


ARDUINO_DIR = /usr/share/arduino
ARDMK_DIR = ~/Documents/Arduino-Makefile
AVR_TOOLS_DIR = /usr/include
BOARD_TAG = uno
# https://gist.github.com/wsh32/19d37709bfb5bea4915e810f03b4f26c
USER_LIB_PATH += ./lib/
# ARDUINO_LIBS = ros_lib RoboClaw Encoder
include $(ARDMK_DIR)/Arduino.mk
