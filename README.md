# POE Portal Turret

### Uploading code via SSH
#### Setup ([reference](https://github.com/sudar/Arduino-Makefile))

On the raspberry pi:
1. `sudo apt install arduino`
2. `pip install pyserial`
3. `cd ~/Documents`
4. `git clone https://github.com/sudar/Arduino-Makefile.git`
5. `cd /usr/share/arduino/libraries`
6. `sudo git clone https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library.git`

#### Usage
To upload code:
1. `cd ~/Documents/POE-Portal-Turret/src/turret_base`
2. `make upload` (Note: to just compile code, you can also just use `make`)


### Raspi Notes
+ Currently using the Raspberry Pi Model B+ V1.2
+ password is portal2rocks
+ connected to olin-devices
+ `ssh -Y pi@pi-bot-amy.local`
+ To shutdown, `sudo shutdown -h now`

### Raspi Camera notes
+ In `sudo raspi-config`, enable I2C and camera under Peripherials option


### References
+ [Accessing PI Camera](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
+ [Using an LCD screen w/ Raspi](https://www.youtube.com/watch?v=cVdSc8VYVBM)