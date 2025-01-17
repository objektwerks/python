# pattern matching
# see https://www.python-engineer.com/posts/pattern-matching-python/

from dataclasses import dataclass
from enum import Enum

def matchOnInt(i: int) -> str:
  match i:
    case _ as n if n < 4: return str(n)
    case _: return f'{i} is outside of range: 0 to 3'

print(f'match on 0 to {matchOnInt(0)}')
print(f'match on 1 to {matchOnInt(1)}')
print(f'match on 2 to {matchOnInt(2)}')
print(f'match on 3 to {matchOnInt(3)}')
print(f'match on 4 to {matchOnInt(4)}')

def matchOnList(ints: list[int]) -> str:
  match ints:
    case [first, *rest]: return f'first: {first}, rest: {rest}'
    case _: return 'unknown'


ints: list[int] = [1, 2, 3]
print(f'match on {ints} to {matchOnList(ints)}')

@dataclass(frozen=True)
class Circle:
  radius: float = 0.0

def matchOnCircle(circle: Circle) -> str:
  match circle:
    case Circle(radius) if radius < 0.0: return 'a diameter of 0.0'
    case Circle(radius): return f'a diameter of {radius * 2}'
    case _: return 'unknown'

circle = Circle(1.5)
print(f'match on {Circle(1.5)} to {matchOnCircle(circle)}')
print(f'match on {Circle()} to {matchOnCircle(Circle())}')

class Color(Enum):
  red = 0
  green = 1
  blue = 2

def matchOnColor(color: Color) -> str:
  match color:
    case Color.red: return 'red'
    case Color.green: return 'green'
    case Color.blue: return 'blue'
    case _: return 'unknown'

color: Color = Color.red
print(f'match on {color} to {matchOnColor(color)}')
