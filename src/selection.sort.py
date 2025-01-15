# selection sort

def findSmallest(items: list[int]):
  firstItem = items[0]
  firstIndex = 0

  for i in range(1, len(items)):
    if items[i] < firstItem:
      firstItem = items[i]
      firstIndex = i

  return firstIndex
