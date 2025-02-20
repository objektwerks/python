# functions

from typing import Callable

def add(ints: list[int]) -> int:
  acc = 0
  for i in ints:
    acc += i
  return acc

odds: list[int] = [1, 2, 3]
print(f'{odds} sum equals {add(ints=odds)}')

def square(i: int = 1) -> int:
  return i * i

two: int = 2
print(f'{two} squared equals {square(two)}')
print(f'default arg squared equals {square()}')

def multiply(multiplier: int) -> Callable[[int], int]:
  return lambda i: i * multiplier

multiplier = multiply(6)
print(f'partial to {multiplier(6)}')