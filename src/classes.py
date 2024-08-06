# classes

class Simple:
  id: str = 'simple'

print(f'simple class: {Simple()}')
print(f'simple class id: {Simple().id}')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f'[Person] name: {self.name} age: {self.age}'

  def speak(self):
    print(f'{self.name} speaking as person ...')

print(f'person: {Person('Fred Flintstone', 27)}')

class Student(Person):
  def __init__(self, name, age, school):
    super().__init__(name, age)
    self.school = school

  def __str__(self):
    return f'[Student] name: {self.name} age: {self.age} school: {self.school}'

  def speak(self):
    print(f'{self.name} speaking as student ...')

print(f'person: {Student('Barney Rubble', 27, 'Rockhurst')}')
