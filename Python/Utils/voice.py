from gtts import gTTS
from playsound import playsound

def voice_over(directory, msg = 'Insira o texto'):
    tts = gTTS(text = msg, lang = 'pt-br', slow=False)
    filename = directory + r'\Sound\voice.mp3'
    tts.save(filename)
    playsound(filename)
