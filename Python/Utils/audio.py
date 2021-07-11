from pygame import mixer

def soundtrack(directory, vol = 1, soundtrack = 0):
    mixer.init()
    mixer.music.stop()
    mixer.music.set_volume(vol) #0 -> 1
    if soundtrack == 0:
        mixer.music.load(directory + '\Sound\soundtrack_00.mp3')
    elif soundtrack == 1:
        mixer.music.load(directory + '\Sound\soundtrack_01.mp3')
    elif soundtrack == 2:
        mixer.music.load(directory + '\Sound\soundtrack_02.mp3')
    elif soundtrack == 3:
        mixer.music.load(directory + '\Sound\soundtrack_03.mp3')

    mixer.music.play(-1)
    return vol

def soundEffect(directory, vol = 1, soundEffect = None):
    if vol > 0 and vol != 1: #Aumentar o som dos efeitos, perante o som do sistema
        vol += 0.2
        if vol > 1:
            vol = 1

    if soundEffect != None:
        if soundEffect == 'Door':
            se = mixer.Sound(directory + '\Sound\sound_effect_Door.wav')
        se.play()
        se.set_volume(vol)
    else:
        print('NONE')

def mixer_pm(vol, plus_or_minus):
    if plus_or_minus == "plus":
        vol += 0.05
    elif plus_or_minus == "minus":
        vol -= 0.05

    if vol > 1:
        vol = 1
    elif vol < 0:
        vol = 0

    mixer.music.set_volume(vol)
    return vol

