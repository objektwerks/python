# selection sort

def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest: smallest = arr[i] smallest_index = i
    Stores the smallest value
    Stores the index of the smallest value

  return smallest_index
