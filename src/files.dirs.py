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

# breadth first search
def traverse(rootdir: str):
  queue = deque()
  queue.append(rootdir)

  while queue:
    dir: str = queue.popleft()
    for file in sorted( os.listdir(dir) ):
      path: str = os.path.join(dir, file)
      if os.path.isfile(path):
        print(file)
      else:
        queue.append(path)

traverse("./src")

# depth first search
def recurse(rootdir: str):
  for file in sorted( os.listdir(rootdir) ):
    path = os.path.join(rootdir, file)
    if os.path.isfile(path):
      print(file)
    else:
      recurse(path)

recurse("./src")
