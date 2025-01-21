# bubble sort

def bubblesort(items: list[int]) -> list[int]:
  unsortedIndex: int = len(items) - 1
  sorted: bool = False

  while not sorted:
    sorted = True
    for i in range(unsortedIndex):
      if items[i] > items[i + 1]:
        items[i], items[i + 1] = items[i + 1], items[i]
        sorted = False
    unsortedIndex -= 1

  return items

ints: list[int] = [3, 2, 1]
print(f'bubble sort on ints {ints} yields: {bubblesort(ints)}')