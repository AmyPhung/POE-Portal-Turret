#include "driveBase.h"


DiffDriveBase::DiffDriveBase(){
  shield.begin();
}

void DiffDriveBase::run(robotCmd cmd){
  // Set limits on command inputs
  if (cmd.f_vel > 100) cmd.f_vel = 100;
  if (cmd.f_vel < -100) cmd.f_vel = -100;
  if (cmd.a_vel > 100) cmd.a_vel = 100;
  if (cmd.a_vel < -100) cmd.a_vel = 100;
  if (cmd.l_shooter > 100) cmd.l_shooter = 100;
  if (cmd.l_shooter < 0) cmd.l_shooter = 0;
  if (cmd.r_shooter > 100) cmd.r_shooter = 100;
  if (cmd.r_shooter < 0) cmd.r_shooter = 0;

  int forward = map(cmd.f_vel, -100, 100, -127, 127);
  int turn = map(cmd.a_vel, -100, 100, -127, 127);    // Left is positive, RH rule
  int l_shoot_speed = map(cmd.l_shooter, 0, 100, 0, 255);
  int r_shoot_speed = map(cmd.r_shooter, 0, 100, 0, 255);

  int Rspeed = forward + turn; // Speed goes from 0 to 255
  int Lspeed = forward - turn;

  if (Rspeed < 0) {
    RMotor->setSpeed(-Rspeed);
    RMotor->run(BACKWARD);  // Backwards
  } else {
    RMotor->setSpeed(Rspeed);
    RMotor->run(FORWARD);  // Forward
  }
  if (Lspeed < 0) {
    LMotor->setSpeed(-Lspeed);
    LMotor->run(BACKWARD);  // Backwards
  } else {
    LMotor->setSpeed(Lspeed);
    LMotor->run(BACKWARD);  // Forward
  }

  LShooter->setSpeed(l_shoot_speed);
  LShooter->run(FORWARD);
  RShooter->setSpeed(r_shoot_speed);
  RShooter->run(FORWARD);
}
