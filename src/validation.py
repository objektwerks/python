# pydantic

from datetime import date
from enum import Enum
from pydantic import BaseModel

class Gender(Enum):
  male = 1
  female = 2

class Person(BaseModel):
  name: str
  born: date
  gender: Gender

print(f'pydantic class: {Person(name = "Fred Flintstone", born = date(2001, 1, 1), gender = Gender.male)}')
