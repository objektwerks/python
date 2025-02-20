# pyttsx3 text-to-speach

import pyttsx3 as tts
from pyttsx3.voice import Voice

engine = tts.init()

text: str = "These words will be converted from text to speech."

# Rate
print(f'rate of speaking is set at: {engine.getProperty('rate')}')
engine.setProperty('rate', 125)
print(f'rate of speaking has been adjusted to: {engine.getProperty('rate')}') # bug! not picking up new rate!

# Volume
print(f'speaking volume is set at: {engine.getProperty('volume')}')
engine.setProperty('volume', 0.75)
print(f'speaking volume has been adjusted to: {engine.getProperty('volume')}') # bug! not picking up new volume!

# Default Voice
engine.say(text)

# Voice
voices: list[Voice] = engine.getProperty('voices')
for voice in voices:
  print(f'speaking voices: {voice.name}')
  if voice.name == "Daniel":
    engine.setProperty('voice', voice.id)
    engine.say(text)

engine.runAndWait()
engine.stop()