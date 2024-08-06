# lambdas
from typing import Callable

sqrt: Callable[[int], int] = lambda i: i * i

print(f'sqrt of 2 equals {sqrt(2)}')
