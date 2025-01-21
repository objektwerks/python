# queue

class Queue:
  def __init__(self):
    self.data = []

  def enqueue(self, element: int) -> None:
    self.data.append(element)

  def dequeue(self) -> int:
    if len(self.data) > 0:
      return self.data.pop(0)
    else:
      return int('-inf')
    
  def len(self) -> int:
    return len(self.data)