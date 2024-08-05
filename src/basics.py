# strings

name: str = 'Fred Flintstone'
age: int = 27
person: str = f'f-string: {name} is {age}.'
print(person)

one: int = 1
print(f'str cast: {str(one)}')
print(f'int cast: {int(one)}')
print(f'float cast: {float(one)}')

twoj: complex = 2j
print(f'complex type: {type(twoj)}')
print(f'type: {type(one)}')

print(f'array[0] = {name[0]}')
print(f'len: {len(person)}')
print(f'slice: {person[10:15]}')
print(f'split: {name.split(' ')}')

print('Barney Rubble' not in person)
print(f'boolean: 2 > 1 = {2 > 1}')

for c in "abc".upper():
  print(c)

print('escape: I am \'Fred\'!')

multilineComment: str = '''
multiline:
that fails to format
correctly as expected.
'''.strip()
print(multilineComment)
