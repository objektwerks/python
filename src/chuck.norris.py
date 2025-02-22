# Chuck Norris jokes via text-to-speech.

import json
import requests
import pyttsx3 as tts
from pyttsx3 import Engine

api: str = "https://api.chucknorris.io/jokes/random"
responseAsJson: str = requests.get(api).text
joke: str = json.loads(responseAsJson)['value']
print(f'joke:\n {joke}')

engine: Engine = tts.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 0.75)
engine.say(joke)
engine.runAndWait()
engine.stop()