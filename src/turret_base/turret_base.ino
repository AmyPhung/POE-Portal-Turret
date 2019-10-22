//#include "turret_base.h"
#include "driveBase.h"
#include <Arduino.h>

DiffDriveBase d;
robotCmd cmd;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  d.setup();
  Serial.println("setup");
  
}

void loop() {
  // If new command has been recieved
  if (Serial.available() > 0) {
    if (Serial.read() == 'c') { // c will be sent for a new cmd
      cmd = readSerial();
      d.run(cmd);
    } else {
      return;
    }
  }
}

robotCmd readSerial() {
  robotCmd cmd_out;

  while (Serial.available() <= 0) { delay(1);}
  char data = Serial.read();
  if (data == '\r') {
    Serial.println("ahshafs");
  }
  Serial.println(data);
  if (data == 'f') {
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'a') {
        break;
      }
      cmd_out.f_vel_str += data;
    }
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'r') {
        break;
      }
      cmd_out.a_vel_str += data;
    }
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'l') {
        break;
      }
      cmd_out.r_shooter_str += data;
    }
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'e') {
        break;
      }
      cmd_out.l_shooter_str += data;
    }
  }

  cmd_out.f_vel = cmd_out.f_vel_str.toInt();
  cmd_out.a_vel = cmd_out.a_vel_str.toInt();
  cmd_out.r_shooter = cmd_out.r_shooter_str.toInt();
  cmd_out.l_shooter = cmd_out.l_shooter_str.toInt();

  Serial.println(cmd_out.f_vel);
  Serial.println(cmd_out.a_vel);
  Serial.println(cmd_out.r_shooter);
  Serial.println(cmd_out.r_shooter);
  return cmd_out;
}




/*

Command (twist-like message)
create a struct for this

get commands via something (serial for now )

WASD from laptop (higher-level behavior)


*/
