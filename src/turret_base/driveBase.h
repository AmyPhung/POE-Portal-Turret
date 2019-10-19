#ifndef DRIVEBASE_H
#define DRIVEBASE_H

#include "msgs.h"
#include <Arduino.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

class DiffDriveBase{
public:
  DiffDriveBase();
  void run(moveCmd cmd);

private:
  Adafruit_MotorShield shield = Adafruit_MotorShield();
  Adafruit_DCMotor *LMotor = shield.getMotor(1);
  Adafruit_DCMotor *RMotor = shield.getMotor(2);
};

#endif
