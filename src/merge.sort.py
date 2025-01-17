# merge sort

def mergesort(items: list[int]):
  if len(items) > 1:
    itemsLen = len(items)
    leftItems = items[:itemsLen]
    rightItems = items[itemsLen:]

    mergesort(leftItems)
    mergesort(rightItems)

    i = j = k = 0

    while i < len(leftItems) and j < len(rightItems):
      if leftItems[i] < rightItems[j]:
        items[k] = leftItems[i]
        i += 1
      else:
        items[k] = rightItems[j]
        j += 1
      k += 1

    while i < len(leftItems):
      items[k] = leftItems[i]
      i += 1
      k += 1

    while j < len(rightItems):
      items[k] = rightItems[j]
      j += 1
      k += 1
