# selection sort - O(n^2)

def findSmallestItemIndex(items: list[int]) -> int:
  findItem: int = items[0]
  findIndex: int = 0

  for index in range(1, len(items)):
    if items[index] < findItem:
      findItem = items[index]
      findIndex = index

  return findIndex

def selectionSort(items: list[int]) -> list[int]:
  newItems: list[int] = []
  copyOfItems: list[int] = list(items)

  for i in range(len(copyOfItems)):
    smallestItem: int = findSmallestItemIndex(copyOfItems)
    newItems.append( copyOfItems.pop(smallestItem) )

  return newItems

ints: list[int] = [5, 3, 6, 2, 10]
print(f'selection sort on ints {ints} to: {selectionSort(ints)}')