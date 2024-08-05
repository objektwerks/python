# strings

multilineComment: str = """
    multiline comment:
    that fails to format
    correctly.
""".strip()
print(multilineComment)

name: str = 'Fred Flintstone'
age = 27
person = f'f-string: {name} is {age}.'
print(person)

print(f'len: {len(person)}')
print(f'slice: {person[10:15]}')