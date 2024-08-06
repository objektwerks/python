# dataclasses
from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    make: str
    model: str
    year: int

print(f'car: {Car('porsche', '911', 2024)}')

@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
