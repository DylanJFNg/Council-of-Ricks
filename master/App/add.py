from pygame import mixer
import time
while True:
    mixer.init(22050, -8, 4, 65536)
    mixer.music.load('ww.ogg')
    mixer.music.play(0)
    time.sleep(1.25)
