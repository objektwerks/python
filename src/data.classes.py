# dataclasses
from dataclasses import dataclass

@dataclass
class Car:
    make: str
    model: str
    year: int

print(f'car: {Car('porsche', '911', 2024)}')
