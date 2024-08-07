# fp - functional programming

from functools import partial, reduce
from typing import Callable

ints: list[int] = [1, 2, 3]

square: Callable[[int], int] = lambda i: i * i

squares: map = map(square, ints)
print(f'map(square,{ints}) to {list(squares)}')

even: Callable[[int], bool] = lambda i: i % 2 == 0

evens: filter = filter(even, ints)
print(f'filter(even,{ints}) to {list(evens)}')

add: Callable[[int, int], int] = lambda x, y: x + y

total: int = reduce(add, ints)
print(f'reduce {ints} to {total}')

def power(base: int, exponent: int) -> int:
  return base ** exponent

cube: partial[int] = partial(power, exponent=3)
print(f'partial {cube} to {cube(base=2)}')
