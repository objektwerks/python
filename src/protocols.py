# protocols

from typing import Protocol

class Animal(Protocol):
  def speak(self) -> str:
    return 'override me!'

class Bear(Animal):
  def speak(self) -> str:
    return 'growl'
  
class Cat(Animal):
  def speak(self) -> str:
    return 'meow'
  
