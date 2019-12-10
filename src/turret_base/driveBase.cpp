#include "driveBase.h"
#define MAX_SPEED 200
#define MAX_TURN 130
#define RIGHT_OFFSET 1   // To account for different speeds
#define LEFT_OFFSET 0.7

DiffDriveBase::DiffDriveBase(){

}

void DiffDriveBase::setup(){
  shield.begin();
  feedServo.attach(10);
  feedServo.write(84); // Start off stopped
}

void DiffDriveBase::run(robotCmd *cmd){
  // Set limits on command inputs
  if (cmd->f_vel > 100) cmd->f_vel = 100;
  if (cmd->f_vel < -100) cmd->f_vel = -100;
  if (cmd->a_vel > 100) cmd->a_vel = 100;
  if (cmd->a_vel < -100) cmd->a_vel = 100;
  if (cmd->l_shooter > 100) cmd->l_shooter = 100;
  if (cmd->l_shooter < 0) cmd->l_shooter = 0;
  if (cmd->r_shooter > 100) cmd->r_shooter = 100;
  if (cmd->r_shooter < 0) cmd->r_shooter = 0;
  if (cmd->feed > 100) cmd->feed = 100;
  if (cmd->feed < -100) cmd->feed = -100;

  int forward = map(cmd->f_vel, -100, 100, -MAX_SPEED, MAX_SPEED);
  int turn = map(cmd->a_vel, -100, 100, -MAX_TURN, MAX_TURN);    // Left is positive, RH rule
  int l_shoot_speed = map(cmd->l_shooter, 0, 100, 0, 255);
  int r_shoot_speed = map(cmd->r_shooter, 0, 100, 0, 255);
  int feed = map(cmd->feed, -100, 100, 0, 168);

  int Rspeed = RIGHT_OFFSET*(forward + turn); // Speed goes from 0 to 255
  int Lspeed = LEFT_OFFSET*(forward - turn);

  if (Rspeed < 0) {
    RMotor->setSpeed(-Rspeed);
    RMotor->run(BACKWARD); 
  } else {
    RMotor->setSpeed(Rspeed);
    RMotor->run(FORWARD); 
  }
  if (Lspeed < 0) {
    LMotor->setSpeed(-Lspeed);
    LMotor->run(FORWARD); // Actually backward
  } else {
    LMotor->setSpeed(Lspeed);
    LMotor->run(BACKWARD); // Actually forward
  }

  analogWrite(l_shooter_pin, l_shoot_speed); // Can go from 0 to 255
  analogWrite(r_shooter_pin, r_shoot_speed); // Can go from 0 to 255

  // LShooter->setSpeed(l_shoot_speed);
  // LShooter->run(BACKWARD); // Actually Forwards
  // RShooter->setSpeed(r_shoot_speed);
  // RShooter->run(FORWARD);

  feedServo.write(feed);
}
