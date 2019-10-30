from mpu6050 import mpu6050
import simpleaudio as sa
import random
import time


# accelerometer z-axis threshold (m/s^2)
# beneath this threshold robot is said to be tilting/falling
Z_ACCEL_THRESHOLD = 9

if name if __name__ == "__main__":

    imu = mpu6050(0x68)

    while True:
        accel_data = imu.get_accel_data()
        filename = 'Turret_turret_tipped_'

        if accel_data['z'] < Z_ACCEL_THRESHOLD:
            # play screaming sound
            filename += (str(random.randint(1,6))+'.wav')
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            time.sleep(random.random())
