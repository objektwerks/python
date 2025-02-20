# pyttsx3 text-to-speach

import pyttsx3 as tts

engine = tts.init()

# Rate of speaking.
print(f'rate of speaking is set at: {engine.getProperty('rate')}')
engine.setProperty('rate', 125)
print(f'rate of speaking has been adjusted to: {engine.getProperty('rate')}')

engine.say("These words will be converted from text to speech.")

engine.runAndWait()