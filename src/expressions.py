# expression - functional programming library

from expression import Nothing, Ok, compose, curry, effect, pipe, Some, Option, Failure, Success, Try
from expression.collections import seq, Seq
from typing import Callable, Generator

@curry(1)
def add(x: int, y: int) -> int:
  return x + y

print(f'curry function to {add(1)(2)}')

value: int = 1
function1: Callable[[int], int] = lambda i: i + 1
function2: Callable[[int], int] = lambda i: i + 2

piped: int = pipe(value, function1, function2)
composed: int = function2(function1(value))

print(f'function1: {function1(value)}')
print(f'function2: {function2(value)}')

print(f'pipe(value, function1, function2): {piped}')
print(f'function2(function1(value)): {composed}')
print(f'piped vs composed equal: {piped == composed}')

some: Option[int] = Some(1)
function3: Callable[[Option[int]], Option[int]] = lambda option: option.map(lambda i: i + 1)
function4: Callable[[Option[int]], Option[int]] = lambda option: option.map(lambda i: i + 2)

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

fluent: int = ints.map(transform).filter(predicate).fold(fold, 0)
print(f'fluent seq map filter fold: {fluent}')

def divide(dividend: int, divisor: int) -> Try[float]:
  if divisor == 0:
    return Failure(Exception("divisor is 0"))
  else:
    return Success(dividend / divisor)

def validate(dividend: int, divisor: int) -> float:
  match divide(dividend, divisor):
    case Try(tag="ok", ok=ok):
      return float(ok)
    case Try(error=error):
      print(error)
      return 0

print(f'try 4 / 2 should equal 2: {validate(4, 2) == 2}')
print(f'try 4 / 0 should equal 0: {validate(4, 0) == 0}')

def check(dividend: int, divisor: int) -> Option[float]:
  match divide(dividend, divisor):
    case Try(tag="ok", ok=ok):
      return Some(ok)
    case Try(error=error):
      print(error)
      return Nothing

print(f'option 4 / 2 should equal 2: {check(4, 2) == Some(2)}')
print(f'option 4 / 0 should equal 0: {check(4, 0) == Nothing}')

print(f'Some(1).value equals: {Some(1).value}')
print(f'Nothing equals: {Nothing}')

@effect.option[int]()
def optionEffect(i: int) -> Generator[int, int, int]:
  x: int = yield i
  y: int = yield from Some(x + 1)
  return x + y

print(f'option effect: {optionEffect(1).value}')

@effect.result[int, Exception]()
def resultEffect(i: int) -> Generator[int, int, int]:
  x: int = yield from Ok(i)
  y: int = yield from Ok(x + 1)
  return x + y

print(f'result effect: {resultEffect(1).ok}')