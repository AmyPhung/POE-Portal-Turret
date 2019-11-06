# POE Portal Turret

### Uploading code via SSH
#### Setup ([reference](https://github.com/sudar/Arduino-Makefile))

On the Euclid:
1. cd /intel/euclid/euclid_ws/src
2. git clone https://github.com/AmyPhung/portal_turret.git
3. cd /intel/euclid/euclid_ws
4. catkin_make


1. `sudo apt install arduino`
2. `pip install pyserial`
3. `cd ~/Documents`
4. `git clone https://github.com/sudar/Arduino-Makefile.git`
5. `cd /usr/share/arduino/libraries`
6. `sudo git clone https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library.git`

cd /intel/euclid/euclid_ws/src/portal_turret/src/turret_base



export ROS_MASTER_URI=http://10.42.0.1:11311
export ROS_IP=10.42.0.219
Ip address is ifconfig on your computer 10.42.0.219

rosrun portal_turret GuiWindow.py

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
+ `ssh -X pi@pi-bot-amy.local`
+ To shutdown, `sudo shutdown -h now`

### Raspi Camera notes
+ In `sudo raspi-config`, enable I2C and camera under Peripherials option


### References
+ [Accessing PI Camera](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
+ [Using an LCD screen w/ Raspi](https://www.youtube.com/watch?v=cVdSc8VYVBM)

### Other Notes
+ Moved away from using keyboard since it requires sudo, which caused strange permission errors. Here are some references that helped me make progress, but overall it wasn't worth it in the end. New iteration uses tkinter keypresses and buttons as a fallback option
+ [SU error]( https://unix.stackexchange.com/questions/110558/su-with-error-x11-connection-rejected-because-of-wrong-authentication)
+ Need to run with sudo
+ Sending keypresses over SSH https://askubuntu.com/questions/358934/sending-keypresses-to-remote-x-session-over-ssh


### Misc notes to be sorted through

ssid=hotspot
#ssid=OLIN-DEVICES
#ROS_MASTER_URI:http://10.0.2.15:11311
ROS_MASTER_URI:http://10.42.0.1:11311
ConnectivityMonitor=55516
LEDServer=38298
SoundServer=43922

After connecting (shouldn't need this):
sudo service oobe-init restart-oobe


settings.ini File:

ssid=hotspot
ROSMasterURI=http://10.42.0.1:11311
ConnectivityMonitor=55516
LEDServer=38298
SoundServer=43922


On laptop:
export ROS_MASTER_URI=http://10.42.0.1:11311
export ROS_IP=http://10.42.0.1:11311

/camera/color/image_raw/compressed
/camera/fisheye/image_raw/compressed
/camera/imu_raw
/camera/ir2/image_raw/compressed
/camera/ir/image_raw/compressed
/camera/depth/points
/camera/depth/image_raw



/camera/color/image_raw/compressed /camera/fisheye/image_raw/compressed /camera/imu_raw /camera/ir2/image_raw/compressed /camera/ir/image_raw/compressed /camera/depth/points /camera/depth/image_raw


Notes:
Why new sensors?
Why ROS?
Why new structure?
