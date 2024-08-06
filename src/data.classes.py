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
pos_two = Pos('a', 1.0, 1.0)
pos_three = Pos('b', 1.0, 2.0)

print(f'{pos_one} eq {pos_two} : {pos_one.__eq__(pos_two)}')
print(f'{pos_one} eq {pos_three} : {pos_one.__eq__(pos_three)}')
