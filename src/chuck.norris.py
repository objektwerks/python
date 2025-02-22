# Chuck Norris jokes via text-to-speech.

import requests
from requests import Response

joke: str = requests.get("https://randomuser.me/api/").text
print(f'joke:\n {joke}')