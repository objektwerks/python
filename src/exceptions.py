# exceptions

def openFile(file: str, options: str) -> str:
  with open(file, options) as f:
    return f.read()

data: str
try:
  data = openFile('requirements.txt', 'r')
except:
  data = 'file not found'

print(f'opened requirements.txt file: {data}')
