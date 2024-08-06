# control

one: int = 1
two: int = 2

if one > two:
    print(f'{one} is greater than {two}')
elif two > one:
    print(f'{two} is greater than {one}')
else:
    print(f'{two} and {one} must be equal')
