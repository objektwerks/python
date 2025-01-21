# stack

class Stack:
  def __init__(self):
    self.data = []

  def push(self, element: int) -> None:
    self.data.append(element)

  def pop(self) -> int:
    if len(self.data) > 0:
      return self.data.pop()
    else:
      return int('-inf')
    
  def len(self) -> int:
    return len(self.data)
    
ints: Stack = Stack()
ints.push(1)
ints.push(2)
ints.push(3)
print(f'stack push on [1, 2, 3] equal len of: {ints.len()}')
ints.pop()
ints.pop()
ints.pop()
print(f'stack pop off [1, 2, 3] equal len of: {ints.len()}')