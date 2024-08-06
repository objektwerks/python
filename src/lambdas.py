# lambdas
from typing import Callable

square: Callable[[int], int] = lambda i: i * i

print(f'sqrt of 2 equals {square(2)}')
