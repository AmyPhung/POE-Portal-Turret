#include "turret_base.h"

DiffDriveBase d;
moveCmd cmd;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  cmd.f_vel = 1;
  cmd.a_vel = 1;
  d.run(cmd);
}


/*

Command (twist-like message)
create a struct for this

get commands via something (serial for now )

WASD from laptop (higher-level behavior)


*/
