# selections sort x - O(n^2)


def selectionSort(items):
  for i in range(len(items) - 1):
              lowest_number_index = i

  for j in range(i + 1, len(items)):
    if items[j] < items[lowest_number_index]:
      lowest_number_index = j
    if lowest_number_index != i:
      items[i], items[lowest_number_index] = items[lowest_number_index], items[i]
    
  return items