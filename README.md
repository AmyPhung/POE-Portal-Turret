# POE Portal Turret

This repository contains code for a portal turret that shoots foam balls at a target.

## Architecture
V1:
+ Used a raspi as main computing device
+ Used a picam to detect people
+ Was pretty slow (~3s lag) for detecting people with full resolution images, was alright with very coarse images (~0.5s lag)

V2:
+ Uses an Intel Euclid as main computing device

## One-Time Setup
#### Local
On your computer, you will need:
+ ROS Kinetic
+ Ubuntu 16 (strongly recommended)

Assuming you have the proper dependencies installed, to set up this repository
+ `cd ~/catkin_ws/src`
+ `git clone https://github.com/AmyPhung/POE-Portal-Turret`
+ `cd ~/catkin_ws`
+ `catkin_make`

+ `pip2 install face_recognition`
https://github.com/ros-drivers/video_stream_opencv

#### Euclid
To get the most recent version of the code on the Euclid, follow these instructions:

On the Euclid:
1. `cd /intel/euclid/euclid_ws/src`
2. `git clone https://github.com/AmyPhung/portal_turret.git`
3. `cd /intel/euclid/euclid_ws`
4. `catkin_make`

## Connecting to the Euclid
In order to connect to the Euclid via ssh, follow the following instructions:
+ Plug in the Euclid and power it on
+ Wait until the network EUCLID_50AB shows up and connect to it
+ SSH into the Euclid using the command `ssh euclid@EUCLID50AB.local`. Password is still the default.
+ On your local computer, you should be able to go to http://10.42.0.1/ in a web browser and see an interface to work with the Euclid.
+ On your local computer, run the following commands to properly configure ROS (note that this will only apply to the terminal you run them in - you will need to run this for each terminal you plan to use to interface with the Euclid)
```
export ROS_MASTER_URI=http://10.42.0.1:11311
export ROS_IP=10.42.0.219
# Note: The ip address you use for the ROS_IP should be the output of the command "ifconfig" on your local machine
```

## Uploading code via SSH
It is much more convenient to upload code remotely to the Arduino by using the Euclid rather than manually having to plug your laptop into the Arduino and using the IDE every time you just want to make a small code change. I've documented this setup process here for future reference.

#### One-Time Setup ([reference](https://github.com/sudar/Arduino-Makefile))
1. `sudo apt install arduino`
2. `pip install pyserial`
3. `cd ~/Documents`
4. `git clone https://github.com/sudar/Arduino-Makefile.git`
5. `cd /usr/share/arduino/libraries`
6. `sudo git clone https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library.git`

#### Usage (Uploading new changes)
To upload new code:
1. `cd /intel/euclid/euclid_ws/src/portal_turret/src/turret_base`
2. `make upload` (Note: to just compile code, you can also just use `make`)

## Running Code
Assuming everything is set up properly you should be able to do the following:

#### On the Euclid:
+ `roslaunch portal_turret bringup.launch`
+ Go to http://10.42.0.1/ and activate the PersonView Scenario under the Scenarios tab

#### On your computer
+ Follow the connect to Euclid instructions
+ On your computer run `rosrun portal_turret GuiWindow.py`

#### Other ROS commands
On either machine, you should be able to use ROS commands. Some useful commands are listed below:
+ `rostopic list` - shows all available data currently being published
+ `rostopic echo /topic_name` - prints out data being published to topic
+ `rosnode list` - shows running nodes
+ `rosnode info /node_name` - prints out data type of node and publishers/subscribers associated with node

## Deprecated Notes (refers to Pi)

### Raspi Notes
+ Currently using the Raspberry Pi Model B+ V1.2
+ password is portal2rocks
+ connected to olin-devices
+ `ssh -X pi@pi-bot-amy.local`
+ To shutdown, `sudo shutdown -h now`

### Raspi Camera notes
+ In `sudo raspi-config`, enable I2C and camera under Peripherials option

### Setting up remote code upload on the Pi
On the raspberry pi:
1. `sudo apt install arduino`
2. `pip install pyserial`
3. `cd ~/Documents`
4. `git clone https://github.com/sudar/Arduino-Makefile.git`
5. `cd /usr/share/arduino/libraries`
6. `sudo git clone https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library.git`

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
