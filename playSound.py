import miniaudio
import os


#mp3name = "Untitled document.mp3"
#x = f"{os.path.dirname(__file__)}/Audio Files/{mp3name}"

def playMp3(mp3name):
    stream = miniaudio.stream_file(f"{os.path.dirname(__file__)}/Audio Files/{mp3name}")
    with miniaudio.PlaybackDevice() as device:
        device.start(stream)
        input("Audio file playing in the background. Enter to stop playback: ")
