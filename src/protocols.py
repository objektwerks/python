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

T = TypeVar("T")

