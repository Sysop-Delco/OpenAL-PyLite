import os
os.add_dll_directory(os.getcwd())
from openal import *
import time

class Example(object):
    def __init__(self):
    #load listener
        self.listener = Listener()
    #initialize sound
        self.sound = LoadSound('tone5.wav')
    #load sound player
        self.player = Player()

    #set listener position
        self.listener.position = (320,240,0)
    #set player position
        self.player.position = (0,240,0)

    #load sound into player
        self.player.add(self.sound)
    #enable loop sound so it plays forever
        self.player.loop = True
    #set rolloff factor
        self.player.rolloff = 0.01
    #play sound
        self.player.play()

    #start recording
        self.listener.rec_start()
        print("Recording")

    #capture recorded samples (and number of samples to capture)
        while len(self.listener.samplescaptured) <= 16000:
            self.listener.rec()

    #stop player
        self.player.stop()

    #stop recording
        self.listener.rec_stop()

    #load captured audio sample into a audio buffer for playback
        self.buffer = BufferSound()
        self.buffer.load(self.listener.samplescaptured)
        self.player.remove()
        self.player.add(self.buffer)

    #play captured audio
        print("Playback")
        self.player.play()
        time.sleep(1)

    #clean up resources
        self.player.delete()
        self.sound.delete()
        self.buffer.delete()
        self.listener.delete()


Example()
