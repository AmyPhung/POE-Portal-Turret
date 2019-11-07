from mpu6050 import mpu6050
from pydub import AudioSegment
from pydub.playback import play
import random
import time


sounds = [AudioSegment.from_wav('audio_files/Turret_turret_tipped_' + str(i) + '.wav') for i in range(6)]

# accelerometer z-axis threshold (m/s^2)
# beneath this threshold robot is said to be tilting/falling
Z_ACCEL_THRESHOLD = 7

if __name__ == "__main__":

    imu = mpu6050(0x68)

    while True:
        accel_data = imu.get_accel_data()

        if accel_data['z'] < Z_ACCEL_THRESHOLD:
            # play screaming sound
            play(sounds[random.randint(1,6)])
