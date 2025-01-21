# selection sort - O(n^2)

def findSmallestItem(items: list[int]) -> int:
  firstItem: int = items[0]
  firstIndex: int = 0

  for index in range(1, len(items)):
    if items[index] < firstItem:
      firstItem = items[index]
      firstIndex = index

  return firstIndex

def selectionsort(items: list[int]) -> list[int]:
  newItems: list[int] = []
  copyOfItems: list[int] = list(items)

  for i in range(len(copyOfItems)):
    smallestItem: int = findSmallestItem(copyOfItems)
    newItems.append( copyOfItems.pop(smallestItem) )

  return newItems

ints: list[int] = [5, 3, 6, 2, 10]
print(f'selection sort on ints {ints} to: {selectionsort(ints)}')