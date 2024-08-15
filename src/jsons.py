# json

import json

letters: dict[str, str] = {'name': 'fred flintstone', 'gender': 'male'}
lettersAsJson: str = json.dumps(letters)
print(f'dumps: dict to json: {lettersAsJson}')
print(f'loads: json to dict: {json.loads(lettersAsJson)}')
