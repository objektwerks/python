# stack

class Stack:
  def __init__(self):
    self.data = []

  def push(self, element) -> None:
    self.data.append(element)

  def pop(self) -> int | None:
    if len(self.data) > 0:
      return self.data.pop()
    else:
      return None
    
ints: Stack = Stack()
ints.push(1)
ints.push(2)
ints.push(3)
print(f'stack push [1, 2, 3]: {ints}')
