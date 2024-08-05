# strings

multilineComment: str = """
  multiline comment:
  that fails to format
  correctly.
""".strip()
print(multilineComment)

name: str = 'Fred Flintstone'
age: int = 27
person: str = f'f-string: {name} is {age}.'
print(person)

print(f'array[0] = {name[0]}')
print(f'len: {len(person)}')
print(f'slice: {person[10:15]}')

for c in "abc":
  print(c)