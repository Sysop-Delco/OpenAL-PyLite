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

    #move sound from left to right
        for a in range(0,704,64):
            self.player.position = (a,240,0)
            time.sleep(1)

    #stop player
        self.player.stop()

    #clean up resources
        self.player.delete()
        self.sound.delete()
        self.listener.delete()


Example()
