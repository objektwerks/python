# bubble sort

def sort(array):
  unsortedUntilIndex = len(array) - 1
  sorted = False

  while not sorted:
    sorted = True
    for i in range(unsortedUntilIndex):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        sorted = False
    unsortedUntilIndex -= 1

  return array