# json

import json

letters: dict[str, str] = {'name': 'fred flintstone', 'gender': 'male'}
lettersAsJson: str = json.dumps(letters)
print(f'dict to json: {lettersAsJson}')

