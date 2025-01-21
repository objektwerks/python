# bubble sort

def sort(items: list[int]):
  unsortedUntilIndex = len(items) - 1
  sorted = False

  while not sorted:
    sorted = True
    for i in range(unsortedUntilIndex):
      if items[i] > items[i + 1]:
        items[i], items[i + 1] = items[i + 1], items[i]
        sorted = False
    unsortedUntilIndex -= 1

  return items