# bubble sort - O(n^2)

def sort(items: list[int]) -> list[int]:
  lastUnsortedIndex: int = len(items) - 1
  sorted: bool = False

  while not sorted:
    sorted = True
    for i in range(lastUnsortedIndex):
      if items[i] > items[i + 1]:
        items[i], items[i + 1] = items[i + 1], items[i]
        sorted = False
    lastUnsortedIndex -= 1

  return items

ints: list[int] = [3, 2, 1]
print(f'bubble sort on ints {ints} sorts to: {sort(ints)}')