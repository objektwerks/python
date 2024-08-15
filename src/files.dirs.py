# files and dirs

import os

with open('requirements.txt', 'r') as f:
    data = f.read()
    print(f'read requirements.txt:\n\n{data}')

with open('test.txt', 'w') as f:
    data = 'test data'
    f.write(data)
    print('write text.txt')

os.remove('test.txt')
print('remove text.txt')
