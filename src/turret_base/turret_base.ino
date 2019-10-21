#include "turret_base.h"

DiffDriveBase d;
robotCmd cmd;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // If new command has been recieved
  if (Serial.available() > 0) {
    if (Serial.read() == 'c') { // c will be sent for a new cmd
      cmd.f_vel = Serial.read();
      cmd.a_vel = Serial.read();
      cmd.r_shooter = Serial.read();
      cmd.l_shooter = Serial.read();
      d.run(cmd);
    } else {
      return;
    }
  }
}


/*

Command (twist-like message)
create a struct for this

get commands via something (serial for now )

WASD from laptop (higher-level behavior)


*/
