# exceptions

def openFile(file: str, options: str) -> str:
  with open(file, options) as f:
    return f.read()

data: str
try:
  data = openFile('req.txt', 'r')
  print(f'opened \'req.txt\' file:\n\n{data}')
except FileNotFoundError as error:
  print(f'error: {error}\n')
  data = openFile('requirements.txt', 'r')
  print(f'opened \'requirements.txt\' file:\n\n{data}')
