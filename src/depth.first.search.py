# depth first search - O(v + e)

import os

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