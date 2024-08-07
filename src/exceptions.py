# exceptions

def openFile(file: str, options: str) -> str:
  with open(file, options) as f:
    return f.read()

data: str
try:
  data = openFile('req.txt', 'r')
  print(f'opened \'req.txt\' file:\n\n{data}')
except FileNotFoundError as error:
  print(f'except: {error}\n')
  data = openFile('requirements.txt', 'r')
  print(f'opened: \'requirements.txt\'\n')
finally:
  print(f'finally: ignore\n')

print(f'data:\n\n{data}')

assert(len(data) > 0)

if (len(data) == 0):
  raise Exception(f'raise: data length is zero')
