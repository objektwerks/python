# pydantic

from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, field_validator

class Gender(Enum):
  male = 1
  female = 2

class Person(BaseModel):
  name: str = Field(frozen = True)
  born: date = Field(frozen = True)
  gender: Gender = Field(frozen = True)
  married: bool = Field(frozen = True)

  @field_validator("born")
  @classmethod
  def validateBorn(cls, born: date) -> date:
    today = date.today()
    eighteen = date(today.year - 18, today.month, today.day)
    if born > eighteen:
      raise ValueError("Married couples should be 18 years or older.")
    return born

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
