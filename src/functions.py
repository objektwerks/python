# functions

def add(ints: list[int]) -> int:
  acc = 0
  for i in ints:
    acc += i
  return acc

def square(i: int) -> int:
  return i * i

numbers: list[int] = [1, 2, 3]
print(f'{numbers} sum equals {add(numbers)}')

two: int = 2
print(f'{two} squared equals {square(two)}')
