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
        self.listener.position = (0,0,0)
    #set player position
        self.player.position = (0,0,40)

    #load sound into player
        self.player.add(self.sound)

    #enable loop sound so it plays forever
        self.player.loop = True
    #set rolloff factor
        self.player.rolloff = 0.01
    #play sound
        self.player.play()

    #re-orient the listeners "at" position
        time.sleep(1)
        self.listener.at_orientation = [0.0,0.0,1.0]
        time.sleep(1)
        self.listener.at_orientation = [0.0,-1.0,0.0]
        time.sleep(1)
        self.listener.at_orientation = [0.0,1.0,0.0]
        time.sleep(1)
        self.listener.at_orientation = [-1.0,0.0,0.0]
        time.sleep(1)
        self.listener.at_orientation = [1.0,0.0,0.0]
        time.sleep(1)
        self.listener.at_orientation = [0.0,0.0,-1.0]

    #re-orient the listeners "up" position
        self.listener.up_orientation = [0.0,-1.0,0.0]
        time.sleep(1)
        self.listener.up_orientation = [1.0,0.0,0.0]
        time.sleep(1)
        self.listener.up_orientation = [-1.0,0.0,0.0]
        time.sleep(1)
        self.listener.up_orientation = [0.0,0.0,1.0]
        time.sleep(1)
        self.listener.up_orientation = [0.0,0.0,-1.0]

    #stop player
        self.player.stop()

    #clean up resources
        self.player.delete()
        self.sound.delete()
        self.listener.delete()


Example()
