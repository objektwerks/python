# insertion sort - O(log n)

def insertion_sort(items: list[int]) -> None:
  for index in range(1, len(items)):
    currentItem = items[index]
    currentItemIndex = index - 1

    while currentItemIndex >= 0:
      if items[currentItemIndex] > currentItem:
        items[currentItemIndex + 1] = items[currentItemIndex]
        currentItemIndex = currentItemIndex - 1
      else:
        break
    
    items[currentItemIndex + 1] = currentItem
    
  return None