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
  d.setup();
  strip.begin();
  strip.show();
  Serial.println("setup");

  interval = 1.0/READ_FREQ * 1000;
  Serial.println(interval);
}

void loop() {
  new_loop_time = millis();
  // Serial.println();
  if (new_loop_time - old_loop_time > interval){
    old_loop_time = new_loop_time;


    readSerial(&cmd);
  }
}

void readSerial(robotCmd *cmd_out){
  serial_input = "";
  char data = Serial.read();
  while (data != -1){
    serial_input += data;
    data = Serial.read();
  }

  // Decode String
  Serial.println(serial_input);
}


void clearSerialBuffer() {
  while (Serial.read() >= 0){}  // read characters until there aren't any (-1)
}

  // for (int i=0; i<LED_COUNT; i++) {
  //   strip.setPixelColor(i, 255, 0, 0);
  // }
  // strip.show();
  //
  // // If new command has been recieved
  // if (Serial.available() > 0) {
  //   if (Serial.read() == 'c') { // c will be sent for a new cmd
  //     Serial.println("Recieving message...");
  //     readSerial(&cmd);
  //     // d.run(&cmd);
  //   } else {
  //     return;
  //   }
  // }
  // char data = Serial.read();

  // Serial.println(data);
  //
  // i++;
  // Serial.println(i);
//}

//void readSerial(robotCmd *cmd_out) {
  // char data = Serial.read();
  // data = Serial.read();


  // while (Serial.available() <= 0) { delay(1);}
 //  char data = Serial.read();
 //  //
 //
 // // Reset value
 //  if (data == 'f') {
 //    cmd_out->f_vel_str = "";
 //    while (true) {
 //      // while (Serial.available() <= 0) { delay(1);}
 //      data = Serial.read();
 //      if (data == 'a') {
 //        break;
 //      }
 //      cmd_out->f_vel_str += data;
 //    }
 //  }
  //   cmd_out->a_vel_str = ""; // Reset value
  //   while (true) {
  //     while (Serial.available() <= 0) { delay(1);}
  //     data = Serial.read();
  //     if (data == 'r') {
  //       break;
  //     }
  //     cmd_out->a_vel_str += data;
  //   }
  //   cmd_out->r_shooter_str = ""; // Reset value
  //   while (true) {
  //     while (Serial.available() <= 0) { delay(1);}
  //     data = Serial.read();
  //     if (data == 'l') {
  //       break;
  //     }
  //     cmd_out->r_shooter_str += data;
  //   }
  //   cmd_out->l_shooter_str = ""; // Reset value
  //   while (true) {
  //     while (Serial.available() <= 0) { delay(1);}
  //     data = Serial.read();
  //     if (data == 'd') {
  //       break;
  //     }
  //     cmd_out->l_shooter_str += data;
  //   }
  //   cmd_out->feed_str = ""; // Reset value
  //   while (true) {
  //     while (Serial.available() <= 0) { delay(1);}
  //     data = Serial.read();
  //     if (data == 'e') {
  //       break;
  //     }
  //     cmd_out->feed_str += data;
  //   }
  // }
  //
  // cmd_out->f_vel = cmd_out->f_vel_str.toInt();
  // cmd_out->a_vel = cmd_out->a_vel_str.toInt();
  // cmd_out->r_shooter = cmd_out->r_shooter_str.toInt();
  // cmd_out->l_shooter = cmd_out->l_shooter_str.toInt();
  // cmd_out->feed = cmd_out->feed_str.toInt();

  // Serial.println(data);
  // Serial.println(cmd_out->f_vel);
  // Serial.println(cmd_out->a_vel);
  // Serial.println(cmd_out->r_shooter);
  // Serial.println(cmd_out->r_shooter);
  // Serial.println(cmd_out->feed);
//}




/*

TODO: Add in ramping to prevent over current draw
TODO: Rewrite firmware to use new boards

*/
