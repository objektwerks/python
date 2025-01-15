# selection sort

def findSmallestItem(items: list[int]) -> int:
  firstItem: int = items[0]
  firstIndex: int = 0

  for index in range(1, len(items)):
    if items[index] < firstItem:
      firstItem = items[index]
      firstIndex = index

  return firstIndex

def sort(items: list[int]) -> list[int]:
  newItems = []
  copyOfItems = list(items)

  for i in range(len(copyOfItems)):
    smallestItem: int = findSmallestItem(copyOfItems)
    newItems.append( copyOfItems.pop(smallestItem) )

  return newItems
