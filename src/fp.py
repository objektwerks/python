# functional programming - fp

from functools import reduce
from typing import Callable

ints: list[int] = [1, 2, 3]

square: Callable[[int], int] = lambda i: i * i

squares = map(square, ints)
print(f'map(square,{ints}) to {list(squares)}')

even: Callable[[int], bool] = lambda i: i % 2 == 0

evens = filter(even, ints)
print(f'filter(even,{ints}) to {list(evens)}')

add: Callable[[int, int], int] = lambda x, y: x + y
