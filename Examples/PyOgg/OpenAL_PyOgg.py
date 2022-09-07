import os
os.add_dll_directory(os.getcwd())
from openal import *
import pyogg
import time

class Example(object):
    def __init__(self):
    #load listener
        self.listener = Listener()
    #load ogg file
        tmp = pyogg.VorbisFile("Example.ogg")

        self.buffer = BufferSound()
    #set channels, bitrate, and samplerate
        self.buffer.channels = tmp.channels
        self.buffer.bitrate = 16
        self.buffer.samplerate = tmp.frequency
        self.buffer.length = tmp.buffer_length
        
    #load audio data
        self.buffer.load(tmp.buffer)

    #load sound player
        self.player = Player()
    #load sound into player
        self.player.add(self.buffer)
    #set rolloff factor
        self.player.rolloff = 0.01
    #play sound
        self.player.play()
    #give time for the sound to play
        time.sleep(7)
    #stop player
        self.player.stop()

    #clean up resources
        self.player.delete()
        self.buffer.delete()
        self.listener.delete()

Example()
