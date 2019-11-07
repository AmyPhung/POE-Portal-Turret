from mpu6050 import mpu6050
from pydub import AudioSegment
from pydub.playback import play
import random
import time
from subprocess import call


call(["amixer", "-D", "pulse", "sset", "Master", "100%"])

# accelerometer z-axis threshold (m/s^2)
# beneath this threshold robot is said to be tilting/falling
Z_ACCEL_THRESHOLD = 9

if __name__ == "__main__":

    imu = mpu6050(0x68)

    while True:
        accel_data = imu.get_accel_data()
        filename = 'audio_files/Turret_turret_tipped_'
        print(accel_data)

        if accel_data['z'] < Z_ACCEL_THRESHOLD:
            # play screaming sound
            filename += (str(random.randint(1,6))+'.wav')
            sound = AudioSegment.from_wav(filename)
            play(sound)
            time.sleep(random.random())
