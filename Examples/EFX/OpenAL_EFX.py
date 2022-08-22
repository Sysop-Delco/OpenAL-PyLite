from openal import *
import time

#For more information on EFX Extentions and how to use them, check out the
#OpenAL Effect Extentions Guide:

#http://kcat.strangesoft.net/misc-downloads/Effects%20Extension%20Guide.pdf


class Example(object):
    def __init__(self):
    #load EFX listener
        self.listener = Listener()
    #initialize sound
        self.sound = LoadSound('LQ_Snare Rev.wav')
    #load EFX sound player
        self.player = Player()

    #create an EFX slot for effects
        self.slot = EFXslot()
    #create a reverb effect
        self.effect1 = Reverb()
    #mount the effect into the EFX slot
        self.slot.set_effect(self.effect1)

    #create a filter effect
        self.filter1 = BandpassFilter()
        self.filter1.gain = 0.5
        
    #set listener position
        self.listener.position = (320,240,0)
    #set player position
        self.player.position = (160,240,0)

    #load sound into player
        self.player.add(self.sound)
    #set rolloff factor
        self.player.rolloff = 0.01


    #move sound from left to right
        for a in range(0,15,1):
            if a == 5:
            #connect a source to output through the EFX slot to apply the effect
                self.player.add_effect(self.slot)
            elif a == 10:
            #attach a direct filter to the source
                self.player.add_filter(self.filter1)

            self.player.play()
            time.sleep(1)

    #stop player
        self.player.stop()

    #clean up resources
        self.effect1.delete()
        self.filter1.delete()
        self.player.delete()
        self.slot.delete()
        self.sound.delete()
        self.listener.delete()
        

Example()
