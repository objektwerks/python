# strings

name: str = 'Fred Flintstone'
age: int = 27
person: str = f'f-string: {name} is {age}.'
print(person)

one: int = 1
print(f'str cast: {str(one)}')
print(f'int cast: {int(one)}')
print(f'float cast: {float(one)}')

print(f'type: {type(one)}')

print(f'array[0] = {name[0]}')
print(f'len: {len(person)}')
print(f'slice: {person[10:15]}')
print("Barney Rubble" not in person)

for c in "abc".upper():
  print(c)

multilineComment: str = """
  multiline comment:
  that fails to format
  correctly.
""".strip()
print(multilineComment)