# strings

multilineComment: str = """
    This is a multiline
    comment that fails
    to format correctly.
""".strip()
print(multilineComment)
print()

name: str = 'Fred Flintstone'
age = 27
person = f"{name} is {age}."
print(person)
print()