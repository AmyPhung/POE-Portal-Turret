# POE Portal Turret

### Uploading code via SSH
#### Setup ([reference](https://github.com/sudar/Arduino-Makefile))

On the raspberry pi:
1. `pip install pyserial`
2. `cd ~/Documents`
3. `git clone https://github.com/sudar/Arduino-Makefile.git`



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
