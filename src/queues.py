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
  
ints: Queue = Queue()
ints.enqueue(1)
ints.enqueue(2)
ints.enqueue(3)
print(f'queue enqueue [1, 2, 3] equal len of: {ints.len()}')
ints.dequeue()
ints.dequeue()
ints.dequeue()
print(f'queue dequeue [1, 2, 3] equal len of: {ints.len()}')