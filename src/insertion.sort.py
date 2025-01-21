# insertion sort - O(log n)

def insertionSort(items: list[int]) -> None:
  for index in range(1, len(items)):
    currentItem: int = items[index]
    currentItemIndex: int = index - 1

    while currentItemIndex >= 0:
      if items[currentItemIndex] > currentItem:
        items[currentItemIndex + 1] = items[currentItemIndex]
        currentItemIndex = currentItemIndex - 1
      else:
        break
    
    items[currentItemIndex + 1] = currentItem
    
  return None

ints: list[int] = [5, 3, 6, 2, 10]
insertionSort(ints)
print(f'insertion sort on ints {[5, 3, 6, 2, 10]} to: {ints}')