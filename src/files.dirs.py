# files and dirs

from collections import deque
import os

with open('requirements.txt', 'r') as f:
    data = f.read()
    print(f'read: requirements.txt:\n\n{data}')

with open('test.txt', 'w') as f:
    data = 'test data'
    f.write(data)
    print('write: text.txt\n')

rootpath: str = './'
print("listdir: ./ \n")
for entry in os.listdir(rootpath):
    if os.path.isfile(os.path.join(rootpath, entry)):
        print(entry)

os.remove('test.txt')
print('\nremove: text.txt\n')

def traverse(rootDir: str):
  traverseQueue = deque()
  traverseQueue.append(rootDir)

  while traverseQueue:
    dir: str = traverseQueue.popleft()
    for file in sorted( os.listdir(dir) ):
      path: str = os.path.join(dir, file)
      if os.path.isfile(path):
        print(file)
      else:
        traverseQueue.append(path)

traverse("./src")
