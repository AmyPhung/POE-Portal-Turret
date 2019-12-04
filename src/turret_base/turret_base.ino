#include "turret_base.h"
#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

#define LED_PIN  2
#define LED_COUNT 24
#define READ_FREQ 30 //Hz

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(50); // time to wait for strings (in ms)
  d.setup();
  strip.begin();
  strip.show();
  Serial.println("setup");

  interval = 1.0/READ_FREQ * 1000;
  // Serial.println(interval);
}

void loop() {
  // Color neopixel ring light
  for (int i=0; i<LED_COUNT; i++) {
    strip.setPixelColor(i, 255, 0, 0);
  }
  strip.show();

  new_loop_time = millis();
  // Serial.println();
  if (new_loop_time - old_loop_time > interval){
    old_loop_time = new_loop_time;

    readSerial(&cmd);
    d.run(&cmd);
  }
}

void readSerial(robotCmd *cmd_out){
  String serial_input = Serial.readString();

  // Decode String
  Serial.println(millis());
  Serial.println(serial_input);
  // Serial.println(serial_input.length());


  if (serial_input.charAt(0) != 'f'){
    // Serial.println("Bad input string - ignoring...");
    return;
  }

  // Reset cmd_out strings
  cmd_out->f_vel_str = "";
  cmd_out->a_vel_str = "";
  cmd_out->r_shooter_str = "";
  cmd_out->l_shooter_str = "";
  cmd_out->feed_str = "";

  int curr_cmd = 0;
  for (int i=1; i<serial_input.length(); i++){
    char c = serial_input.charAt(i);
    // Serial.println("New Char:");
    // Serial.println(c);
    if (c == 'a') {curr_cmd = 1; continue;}
    else if (c == 'r') {curr_cmd = 2; continue;}
    else if (c == 'l') {curr_cmd = 3; continue;}
    else if (c == 'd') {curr_cmd = 4; continue;}
    else if (c == 'e') break; // Ignore characters after e

    if (curr_cmd == 0) cmd_out->f_vel_str += c;
    else if (curr_cmd == 1) cmd_out->a_vel_str += c;
    else if (curr_cmd == 2) cmd_out->r_shooter_str += c;
    else if (curr_cmd == 3) cmd_out->l_shooter_str += c;
    else if (curr_cmd == 4) cmd_out->feed_str += c;
  }

  // Convert strings to ints in cmd_out
  cmd_out->f_vel = cmd_out->f_vel_str.toInt();
  cmd_out->a_vel = cmd_out->a_vel_str.toInt();
  cmd_out->r_shooter = cmd_out->r_shooter_str.toInt();
  cmd_out->l_shooter = cmd_out->l_shooter_str.toInt();
  cmd_out->feed = cmd_out->feed_str.toInt();

  Serial.println("Current Commands:");
  Serial.println(cmd_out->f_vel);
  Serial.println(cmd_out->a_vel);
  Serial.println(cmd_out->r_shooter);
  Serial.println(cmd_out->r_shooter);
  Serial.println(cmd_out->feed);
}

/*

TODO: Add in ramping to prevent over current draw
TODO: Rewrite firmware to use new boards

*/
