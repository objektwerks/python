# classes

class Simple:
  id: str = 'simple'

print(f'simple class: {Simple()}')
print(f'simple class id: {Simple().id}')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

print(f'person: {Person('Fred Flintstone', 27)}')
