# pyttsx3 text-to-speach

import pyttsx3 as tts

engine = tts.init()
engine.say("These words will be converted from text to speech.")
engine.runAndWait()