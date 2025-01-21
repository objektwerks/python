# exceptions

try:
  with open('not.there.txt', 'r') as f:
    data = f.read()
    print(f'read: requirements.txt:\n\n{data}')
except FileNotFoundError as error:
  print(f'try / except: {error}')