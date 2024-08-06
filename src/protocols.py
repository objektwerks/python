# protocols

from typing import Protocol, TypeVar

class Animal(Protocol):
  def speak(self) -> str:
    return 'override me!'

class Bear(Animal):
  def speak(self) -> str:
    return 'growl'
  
class Cat(Animal):
  def speak(self) -> str:
    return 'meow'
  
def speak(animal: Animal) -> str:
    return animal.speak()
  
print(f'Bear speak - {Bear().speak()}')
print(f'Cat speak - {Cat().speak()}')

T = TypeVar("T", bound=int | float)

class Adder(Protocol[T]):
  def add(self, x: T, y: T) -> T:
    ...

class IntAdder:
  def add(self, x: int, y: int) -> int:
    return x + y

class FloatAdder:
  def add(self, x: float, y: float) -> float:
    return x + y

def add(adder: Adder, x: T, y: T) -> T:
  return adder.add(x, y)

print(f'add ints 1 and 2 == {add(IntAdder(), 1, 2)}')
print(f'add ints 1 and 2 == {add(FloatAdder(), 1, 2)}')
