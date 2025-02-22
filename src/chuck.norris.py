# Chuck Norris jokes via text-to-speech.

import json
import requests
from requests import Response
import pyttsx3 as tts

api: str = "https://api.chucknorris.io/jokes/random"
responseAsJson: str = requests.get(api).text
joke: str = json.loads(responseAsJson)['value']
print(f'joke:\n {joke}')

engine = tts.init()
