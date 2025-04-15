#A simple script that uses the operating system default Text-To-Speech
from plyer import tts

def say(message):
    tts.speak(message=message)
