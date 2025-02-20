# breadth first search - O(v + e)

from collections import deque
import os
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
    if filter(node):
      filtered.append(node)

    for child in graph[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return filtered

def transform(graph: dict[int, list[int]], start: int, transformer: Callable[[int], int]) -> list[int]:
  queue: deque[int] = deque([start])
  visited: list[int] = []
  transformed: list[int] = []

  while queue:
    node: int = queue.popleft()
    visited.append(node)
    transformed.append( transformer(node) )

    for child in graph[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return transformed

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

def square(number: int) -> int:
  return number * number

print(f'graph {graph}')
print(f'traverse graph in this order: {traverse(graph, 1)}')
print(f'filter graph with the [{isEven.__name__}] filter: {filter(graph, 1, isEven)}')
print(f'transform graph with the [{square.__name__}] transformer: {transform(graph, 1, square)}')

def files(rootdir: str) -> list[str]:
  queue: deque[str] = deque()
  queue.append(rootdir)
  files: list[str] = []

  while queue:
    dir: str = queue.popleft()
    for file in sorted( os.listdir(dir) ):
      path: str = os.path.join(dir, file)
      if os.path.isfile(path):
        files.append(file)
      else:
        queue.append(path)
  return files

print("files:")
print( '\n'.join( files("./src") ) )