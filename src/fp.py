# functional programming - fp

from functools import reduce
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
