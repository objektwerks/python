# requests

import requests
from requests import Response

response: Response = requests.get("https://randomuser.me/api/")
print(f'response: {response.text}')
