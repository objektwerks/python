# json

import json
import os

letters: dict[str, str] = {'name': 'fred flintstone', 'gender': 'male'}
lettersAsJson: str = json.dumps(letters)
print(f'dumps: dict to json: {lettersAsJson}')
print(f'loads: json to dict: {json.loads(lettersAsJson)}')

with open('json.txt', 'w') as f:
    f.write(lettersAsJson)
    print('write: json.txt\n')

rootpath: str = './'
print("listdir: ./ \n")
for entry in os.listdir(rootpath):
    if os.path.isfile(os.path.join(rootpath, entry)):
        print(entry)

