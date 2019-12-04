#ifndef TURRET_BASE_H
#define TURRET_BASE_H

// Libraries
#include "driveBase.h"
#include "msgs.h"
#include <Arduino.h>

DiffDriveBase d;
robotCmd cmd;
unsigned long old_loop_time = millis();
unsigned long new_loop_time = millis(); // Time at last read
int interval;
String serial_input;
void readSerial(robotCmd *cmd_out);

#endif
