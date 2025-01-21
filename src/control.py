# control

one: int = 1
two: int = 2

if one > two:
  print(f'{one} is greater than {two}')
elif two > one:
  print(f'{two} is greater than {one}')
else:
  print(f'{two} and {one} must be equal')

i: int = 1
while i < 4:
  print(i)
  i += 1
else:
  print(f'{i} is no longer less than {i}')

s: str = 'abc'
for s in s:
  print(s)