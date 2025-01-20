# dijkstra's algo

from dataclasses import dataclass

graph: dict[str, dict[str, int]] = {
  's':{'a':8, 'b':4},
  'a':{'b':4},
  'b':{'a':3, 'c':2, 'd':5},
  'c':{'d':2},
  'd':{}
}

@dataclass(frozen=True)
class Node:
  x: int
  y: int
  distance: float = float('inf')
  parent = None
  finished: bool = False
