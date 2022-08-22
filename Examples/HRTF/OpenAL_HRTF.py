from openal import *
import time

#For more information on HRTF tables, visit:
#http://recherche.ircam.fr/equipes/salles/listen/index.html


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
        self.player.position = (0,240,-200)

    #load sound into player
        self.player.add(self.sound)
    #enable loop sound so it plays forever
        self.player.loop = True
    #set rolloff factor
        self.player.rolloff = 0.01
    #play sound
        self.player.play()


    #move sound from left to right (no hrtf)
        for a in range(0,704,64):
            self.player.position = (a,240,-200)
            time.sleep(1)

    #show number of available hrtf tables
        print(self.listener.hrtf_tables)
    #enable hrtf default_44100 table
        self.listener.hrtf = 1
    #check hrtf status to make sure its enabled
        print(self.listener.hrtf)

    #move sound from left to right (hrtf enabled)
        for a in range(0,704,64):
            self.player.position = (a,240,-200)
            time.sleep(1)

    #enable hrtf default_48000 table
        self.listener.hrtf = 2
    #check hrtf status to make sure its enabled
        print(self.listener.hrtf)

    #move sound from left to right (hrtf enabled)
        for a in range(0,704,64):
            self.player.position = (a,240,-200)
            time.sleep(1)

    #stop player
        self.player.stop()

    #clean up resources
        self.player.delete()
        self.sound.delete()
        self.listener.delete()
        


Example()
