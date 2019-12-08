#!/usr/bin/env python3

import speech_recognition as sr
import numpy as np
import time
import wave
import pyaudio
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from mpu6050 import mpu6050

Z_ACCEL_THRESHOLD = 7
p = pyaudio.PyAudio()
state = 'activate'

voice_lines = {'accept':       [wave.open('audio_files/accept/'+str(i)+'.wav','rb') for i in range(3)],
               'activate':     [wave.open('audio_files/activate/'+str(i)+'.wav','rb') for i in range(2)],
               'apology':      [wave.open('audio_files/apology/'+str(i)+'.wav','rb') for i in range(5)],
               'deactivate':   [wave.open('audio_files/deactivate/'+str(i)+'.wav','rb') for i in range(7)],
               'falling':      [wave.open('audio_files/falling/'+str(i)+'.wav','rb') for i in range(8)],
               'firing':       [wave.open('audio_files/firing/'+str(i)+'.wav','rb') for i in range(2)],
               'found_target': [wave.open('audio_files/found_target/'+str(i)+'.wav','rb') for i in range(7)],
               'greeting':     [wave.open('audio_files/greeting/'+str(i)+'.wav','rb') for i in range(4)],
               'idle':         [wave.open('audio_files/idle/'+str(i)+'.wav','rb') for i in range(3)],
               'lonely':       [wave.open('audio_files/lonely/'+str(i)+'.wav','rb') for i in range(7)],
               'lost_target':  [wave.open('audio_files/lost_target/'+str(i)+'.wav','rb') for i in range(4)],
               'reject':       [wave.open('audio_files/reject/'+str(i)+'.wav','rb') for i in range(2)],
               'searching':    [wave.open('audio_files/accept/'+str(i)+'.wav','rb') for i in range(2)]}

def speak(wf = None):
    if wf == None:
        wf = np.random.choice(voice_lines[state])
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
    data = wf.readframes(wf.getnframes())
    stream.write(data)
    stream.close()

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    try:
        print(r.recognize_sphinx(audio, keyword_entries=[("please", 1.0)]))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


if __name__ == "__main__":
    speak()
    state = 'idle'
    anl = SentimentIntensityAnalyzer()

    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)  # only need to calibrate once

    # start listening in the background
    stop_listening = r.listen_in_background(m, callback)
    # `stop_listening` is a callable function that stops background listening

    while True:
        accel_data = imu.get_accel_data()

        if accel_data['z'] < Z_ACCEL_THRESHOLD:
            state = 'falling'
            speak()
        else:
            state = np.random.choice(['idle', 'lonely', 'searching', 'lost_target'])
            speak()
            time.pause(np.random.rand()*5)
