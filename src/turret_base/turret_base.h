#ifndef TURRET_BASE_H
#define TURRET_BASE_H

// Libraries
#include "driveBase.h"
#include "msgs.h"
#include <Arduino.h>

DiffDriveBase d;
robotCmd cmd;
void readSerial(robotCmd *cmd_out);

#endif
