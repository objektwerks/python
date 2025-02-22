# Chuck Norris jokes via text-to-speech.

import json
import requests
from requests import Response

api: str = "https://api.chucknorris.io/jokes/random"
responseAsJson: str = requests.get(api).text
joke: str = json.loads(responseAsJson)['value']
print(f'joke:\n {joke}')