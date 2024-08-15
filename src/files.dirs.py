# files and dirs

import os

with open('requirements.txt', 'r') as f:
    data = f.read()
    print(f'read requirements.txt:\n\n{data}')

with open('test.txt', 'w') as f:
    data = 'test data'
    f.write(data)
    print('write text.txt\n')

os.remove('test.txt')
print('remove text.txt')

rootpath: str = './'
print("listdir ./")
for entry in os.listdir(rootpath):
    if os.path.isfile(os.path.join(rootpath, entry)):
        print(entry)

