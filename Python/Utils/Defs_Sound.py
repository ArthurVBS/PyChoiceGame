from pygame import mixer

def sound(directory, vol, sound = 0):
    mixer.init()
    mixer.music.stop()
    mixer.music.set_volume(vol) #0 -> 1
    if sound == 0:
        mixer.music.load(directory + '/Sound/soundtrack_00.mp3')
    elif sound == 1:
        mixer.music.load(directory + '/Sound/soundtrack_01.mp3')
    elif sound == 2:
        mixer.music.load(directory + '/Sound/soundtrack_02.mp3')
    elif sound == 3:
        mixer.music.load(directory + '/Sound/soundtrack_03.mp3')

    mixer.music.play(-1)
    return vol

def mixer_pm(vol, p_or_m):
    if p_or_m == "plus":
        vol += 0.05
    elif p_or_m == "minus":
        vol -= 0.05

    if vol > 1:
        vol = 1
    elif vol < 0:
        vol = 0

    mixer.music.set_volume(vol)
    return vol
