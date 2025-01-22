# selection sort - O(n^2)

def findSmallestItemIndex(items: list[int]) -> int:
  findItem: int = items[0]
  findIndex: int = 0

  for index in range(1, len(items)):
    if items[index] < findItem:
      findItem = items[index]
      findIndex = index

  return findIndex

def sort(items: list[int]) -> list[int]:
  sortedItems: list[int] = []
  copyOfItems: list[int] = list(items)

  for i in range(len(copyOfItems)):
    smallestItemIndex: int = findSmallestItemIndex(copyOfItems)
    sortedItems.append( copyOfItems.pop(smallestItemIndex) )

  return sortedItems

ints: list[int] = [3, 2, 1]
print(f'selection sort on ints {ints} sorts to: {sort(ints)}')