# dataclasses
from dataclasses import dataclass

@dataclass
class Car:
    model: str
    year: int

print(f'car: {Car('porsche', 2024)}')
