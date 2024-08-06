# dataclasses
from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    make: str
    model: str
    year: int

print(f'car: {Car('porsche', '911', 2024)}')

@dataclass(frozen=True)
class Pos:
    name: str
    lon: float = 0.0
    lat: float = 0.0

pos_one = Pos("a", 1.0, 1.0)
pos_two = Pos('b', 1.0, 1.0)
pos_three = Pos('c', 3.0, 3.0)
