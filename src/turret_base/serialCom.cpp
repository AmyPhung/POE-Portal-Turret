//   SerialConnection()
//
// if(Serial.available() > 0) {
//   if (Serial.read() == 'e') { // e will be sent for an e-stop
//     isEStopped = !isEStopped;
//     lcd.setCursor(6,0);
//     lcd.print(isEStopped);
//   } else {
//     resetLCD();
//     pidValues = readSerial();
//     updateLCD(pidValues);
//   }
// }
