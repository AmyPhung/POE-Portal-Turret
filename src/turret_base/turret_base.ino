#include "turret_base.h"
#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

#define LED_PIN  2
#define LED_COUNT 24

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  d.setup();
  strip.begin();
  strip.show();
  Serial.println("setup");

}

void loop() {
  for (int i=0; i<LED_COUNT; i++) {
    strip.setPixelColor(i, 255, 0, 0);
  }
  strip.show();

  // If new command has been recieved
  if (Serial.available() > 0) {
    if (Serial.read() == 'c') { // c will be sent for a new cmd
      readSerial(&cmd);
      d.run(&cmd);
    } else {
      return;
    }
  }
}

void readSerial(robotCmd *cmd_out) {
  while (Serial.available() <= 0) { delay(1);}
  char data = Serial.read();

  if (data == 'f') {
    cmd_out->f_vel_str = ""; // Reset value
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'a') {
        break;
      }
      cmd_out->f_vel_str += data;
    }
    cmd_out->a_vel_str = ""; // Reset value
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'r') {
        break;
      }
      cmd_out->a_vel_str += data;
    }
    cmd_out->r_shooter_str = ""; // Reset value
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'l') {
        break;
      }
      cmd_out->r_shooter_str += data;
    }
    cmd_out->l_shooter_str = ""; // Reset value
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'd') {
        break;
      }
      cmd_out->l_shooter_str += data;
    }
    cmd_out->feed_str = ""; // Reset value
    while (true) {
      while (Serial.available() <= 0) { delay(1);}
      data = Serial.read();
      if (data == 'e') {
        break;
      }
      cmd_out->feed_str += data;
    }
  }

  cmd_out->f_vel = cmd_out->f_vel_str.toInt();
  cmd_out->a_vel = cmd_out->a_vel_str.toInt();
  cmd_out->r_shooter = cmd_out->r_shooter_str.toInt();
  cmd_out->l_shooter = cmd_out->l_shooter_str.toInt();
  cmd_out->feed = cmd_out->feed_str.toInt();

  // Serial.println(cmd_out->f_vel);
  // Serial.println(cmd_out->a_vel);
  // Serial.println(cmd_out->r_shooter);
  // Serial.println(cmd_out->r_shooter);
  // Serial.println(cmd_out->feed);
  return cmd_out;
}




/*

TODO: Add in ramping to prevent over current draw
TODO: Rewrite firmware to use new boards

*/
