# expression - functional programming library

from expression import compose, curry, pipe, Some, Option
from expression.collections import seq, Seq
from typing import Callable

@curry(1)
def add(x: int, y: int) -> int:
  return x + y

print(f'curry function to {add(1)(2)}')

value: int = 1
function1: Callable[[int], int] = lambda i: i + 1
function2: Callable[[int], int] = lambda i: i + 2

piped = pipe(value, function1, function2)
composed = function2(function1(value))

print(f'function1: {function1(value)}')
print(f'function2: {function2(value)}')

print(f'pipe(value, function1, function2): {piped}')
print(f'function2(function1(value)): {composed}')
print(f'piped vs composed equal: {piped == composed}')

some: Option[int] = Some(1)
function3 = lambda option: option.map(lambda i: i + 1)
function4 = lambda option: option.map(lambda i: i + 2)

print(f'function3: {function3(some)}')
print(f'function4: {function4(some)}')

print(f'pipe(some, function3, function4): {piped}')
print(f'function3(function4(some)): {composed}')
print(f'option piped vs composed equal: {some.pipe(function3, function4) == function4(function3(some))}')

transform: Callable[[int], int] = lambda i: i + 1
predicate: Callable[[int], bool] = lambda i: i % 2 == 0
fold: Callable[[int, int], int] = lambda acc, i: acc + i

ints: Seq[int] = Seq.of(1, 2, 3)
result: int = ints.pipe(
  seq.map(transform),
  seq.filter(predicate),
  seq.fold(fold, 0),
)

print(f'pipe seq map filter fold: {result}')

composeMapFilterFold = compose(
  seq.map(transform),
  seq.filter(predicate),
  seq.fold(fold, 0)
)
print(f'compose seq map filter fold: {composeMapFilterFold(ints)}')
