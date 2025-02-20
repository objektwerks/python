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
def traverse(rootdir: str) -> list[str]:
  queue: deque[str] = deque()
  queue.append(rootdir)
  files: list[str] = []

  while queue:
    dir: str = queue.popleft()
    for file in sorted( os.listdir(dir) ):
      path: str = os.path.join(dir, file)
      if os.path.isfile(path):
        files.append(file)
      else:
        queue.append(path)
  return files

print("traverse:")
print( '\n'.join( traverse("./src") ) )


# depth first search
def recurse(rootdir: str) -> list[str]:
  files: list[str] = []
  for file in sorted( os.listdir(rootdir) ):
    path = os.path.join(rootdir, file)
    if os.path.isfile(path):
      files.append(file)
    else:
      recurse(path)
  return files

print("recurse:")
print( '\n'.join( recurse("./src") ) )