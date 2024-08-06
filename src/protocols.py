# protocols

from typing import Protocol

class Animal(Protocol):
  def speak(self) -> str:
    return 'override me!'

