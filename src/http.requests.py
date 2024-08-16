# requests

import requests
from requests import Response

response: Response = requests.get("https://randomuser.me/api/")
print(f'response status code: {response.status_code}')
print(f'response reason: {response.reason}')
print(f'response text: {response.text}')
