# requests

import requests
from requests import Response

response: Response = requests.get("https://randomuser.me/api/")
print(f'response status code: {response.status_code}')
print(f'response reason: {response.reason}')
print(f'response headers:\n {response.headers}')
print(f'response text:\n {response.text}')
