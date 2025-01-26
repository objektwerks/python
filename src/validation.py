# pydantic

from pydantic import BaseModel

class Person(BaseModel):
  name: str
  age: int

print(f'pydantic class: {Person(name = "Fred Flintstone", age = 24)}')
