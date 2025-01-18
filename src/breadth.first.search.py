# breadth first search

from collections import deque
from typing import Callable

def traverse(graph: dict[int, list[int]], start: int) -> list[int]:
  queue: deque[int] = deque([start])
  visited: list[int] = []

  while queue:
    node: int = queue.popleft()
    visited.append(node)

    for child in graph[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return visited

def filter(graph: dict[int, list[int]], start: int, filter: Callable[[int], bool]) -> list[int]:
  queue: deque[int] = deque([start])
  visited: list[int] = []
  filtered: list[int] = []

  while queue:
    node: int = queue.popleft()
    visited.append(node)
    if filter(node) == True:
      filtered.append(node)

    for child in graph[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return filtered

graph: dict[int, list[int]] = {
  1: [2, 3, 4, 5],
  2: [6, 7],
  3: [8],
  4: [9],
  5: [],
  6: [],
  7: [10],
  8: [],
  9: [],
  10: [1]
}

def isEven(number: int) -> bool:
  return True if number % 2 == 0 else False

print(f'traverse graph {graph} in this order: {traverse(graph, 1)}')
print(f'filter graph {graph} with this filter {isEven}: {filter(graph, 1, isEven)}')
