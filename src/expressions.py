# expression - functional programming library

from expression import curry, pipe
from typing import Callable

@curry(1)
def add(x: int, y: int) -> int:
  return x + y

print(f'curry function to {add(1)(2)}')

value: int = 1
function1: Callable[[int], int] = lambda i: i + 1
function2: Callable[[int], int] = lambda i: i * 2

piped = pipe(value, function1, function2)
composed = function2(function1(value))

print(f'function1: {function1(value)}')
print(f'piped: {piped}')
print(f'composed: {composed}')
print(f'piped vs composed equal: {piped == composed}')
