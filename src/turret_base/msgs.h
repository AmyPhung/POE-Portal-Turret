#ifndef MSGS_H
#define MSGS_H

struct moveCmd {
  int f_vel;   // Forward velocity - between -100 and 100
  int a_vel;   // Angular veloctiy - between -100 and 100
};

// TODO: add turret command here

struct robotCmd {
  moveCmd move_cmd;
};

#endif
