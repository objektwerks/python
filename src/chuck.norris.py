# Chuck Norris jokes via text-to-speech.

import requests
from requests import Response

api: str = "https://api.chucknorris.io/jokes/random"
joke: str = requests.get(api).text
print(f'joke:\n {joke}')