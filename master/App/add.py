from pygame import mixer
import os
import time
while True:
    mixer.init(22050, -8, 4, 65536)
    mixer.music.load('ww.ogg')
    mixer.music.play(0)
    time.sleep(1.15)
    os.system("echo 'shut the door now now now cat' | espeak")