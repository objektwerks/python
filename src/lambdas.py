# lambdas

from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y

one: int = 1
two: int = 2
print(f'{one} plus {two} equals {add(one, two)}')

square: Callable[[int], int] = lambda i: i * i

print(f'square root of 2 equals {square(2)}')

multiply = lambda x: lambda y: x * y
print(f'partial to {multiply(2)(3)}')