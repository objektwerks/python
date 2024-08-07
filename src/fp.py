# functional programming - fp

from typing import Callable

square: Callable[[int], int] = lambda i: i * i

even: Callable[[int], bool] = lambda i: i % 2 == 0

odd: Callable[[int], bool] = lambda i: i % 2 != 0

ints: list[int] = [1, 2, 3]

squares = map(square, ints)
print(f'map(square,{ints}) to {list(squares)}')

evens = filter(even, ints)
print(f'filter(even,{ints}) to {list(evens)}')

odds = filter(odd, ints)