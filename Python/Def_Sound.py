from pygame import mixer

def music(directory):
    mixer.init()
    mixer.music.load(directory + '/Sound/soundtrack.mp3')
    mixer.music.play(-1)
