# functional programming - fp

from typing import Callable

square: Callable[[int], int] = lambda i: i * i

even: Callable[[int], bool] = lambda i: i % 2 == 0

odd: Callable[[int], bool] = lambda i: i % 2 != 0

ints: list[int] = [1, 2, 3]

