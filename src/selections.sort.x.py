# selections sort x - O(n^2)


def selectionSort(items: list[int]) -> list[int]:
  for i in range(len(items) - 1):
    lowestNumberIndex = i

    for j in range(i + 1, len(items)):
      if items[j] < items[lowestNumberIndex]:
        lowestNumberIndex = j
      if lowestNumberIndex != i:
        items[i], items[lowestNumberIndex] = items[lowestNumberIndex], items[i]
    
  return items