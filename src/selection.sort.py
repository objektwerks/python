# selection sort

def findSmallest(items: list[int]) -> int:
  firstItem = items[0]
  firstIndex = 0

  for index in range(1, len(items)):
    if items[index] < firstItem:
      firstItem = items[index]
      firstIndex = index

  return firstIndex
