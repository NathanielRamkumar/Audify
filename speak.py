import gtts
import os

def tts(txtname, mp3name):
    with open(f"{os.path.dirname(__file__)}/Txt Files/{txtname}", 'r') as file:
        text =  file.read()

    tts = gtts.gTTS(text, lang='en')
    tts.save(f"{os.path.dirname(__file__)}/Audio Files/{mp3name}")

