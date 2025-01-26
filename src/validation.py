# pydantic

from datetime import date
from enum import Enum
from typing import Self
from pydantic import BaseModel, Field, field_validator, model_validator

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
  def validateMarried(cls, born: date) -> date:
    today: date = date.today()
    eighteen: date = date(today.year - 18, today.month, today.day)
    print(f'[validateMarried] born: {born} eighteen: {eighteen} is valid: {eighteen > born}')
    if born > eighteen:
      raise ValueError("Married couples must be 18 years of age or older.")
    return born
  
  @model_validator(mode = "after")
  def validateJson(self) -> Self:
    print(f'[validateJson] pydantic class as json: {self.model_dump_json()}')
    return self

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
