#Import - Libraries _________________________________________________________________________________________

from pygame import mixer

#Functions - Sound __________________________________________________________________________________________

def soundEffect(directory, soundEffect = None):
    mixer.init()

    if soundEffect != None:
        se = mixer.Sound(directory + f'/Sounds/sound_effect_{soundEffect}_Mario.wav')
        se.play()
        se.set_volume(1)
    else:
        print('NONE')
