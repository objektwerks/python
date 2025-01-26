# pydantic

from enum import Enum
from pydantic import BaseModel

class Gender(Enum):
  male = 1
  female = 2

class Person(BaseModel):
  name: str
  age: int
  gender: Gender

print(f'pydantic class: {Person(name = "Fred Flintstone", age = 24, gender = Gender.male)}')
