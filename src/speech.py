# pyttsx3 text-to-speach

import pyttsx3 as tts

engine = tts.init()

# Rate
print(f'rate of speaking is set at: {engine.getProperty('rate')}')
engine.setProperty('rate', 125)
print(f'rate of speaking has been adjusted to: {engine.getProperty('rate')}') # bug! not picking up new rate!

# Volume
print(f'speaking volume is set at: {engine.getProperty('volume')}')
engine.setProperty('volume', 0.75)
print(f'speaking volume has been adjusted to: {engine.getProperty('volume')}') # bug! not picking up new volume!

engine.say("These words will be converted from text to speech.")

engine.runAndWait()
engine.stop()