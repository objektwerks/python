# selection sort

def findSmallestItem(items: list[int]) -> int:
  firstItem: int = items[0]
  firstIndex: int = 0

  for index in range(1, len(items)):
    if items[index] < firstItem:
      firstItem = items[index]
      firstIndex = index

  return firstIndex

def selectionSort(arr):
  newArr = []
  copiedArr = list(arr)
  for i in range(len(copiedArr)):
    smallest = findSmallestItem(copiedArr)
    newArr.append(copiedArr.pop(smallest))
    return newArr
