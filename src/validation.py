# pydantic

from datetime import date
from enum import Enum
from pydantic import BaseModel, Field

class Gender(Enum):
  male = 1
  female = 2

class Person(BaseModel):
  name: str = Field(frozen = True)
  born: date = Field(frozen = True)
  gender: Gender = Field(frozen = True)
  married: bool = Field(frozen = True)

person: Person = Person(
  name = "Fred Flintstone",
  born = date(2001, 1, 1),
  gender = Gender.male,
  married = True
)
print(f'pydantic class: {person}')

personAsJson: str = person.model_dump_json()
print(f'pydantic class as json: {personAsJson}')

personFromJson: Person = Person.model_validate_json(personAsJson)
print(f'pydantic class derived from json: {personFromJson}')

updatedPerson: Person = person.model_copy(update={'born': date(2001, 1, 2)})
print(f'pydantic class updated via copy: {updatedPerson}')
