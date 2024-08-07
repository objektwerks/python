# exceptions

def openFile(file: str, options: str) -> str:
  with open('data.txt', 'r') as f:
    return f.read()

data: str
try:
  data = openFile('requirements.txt', 'r')
  print(f'data: {data}')
except:
  data = 'file not found'

print(f'opened requirements.txt file: {data}')
