# dijkstra's algo

graph: dict[str, dict[str, int]] = {
  's':{'a':8, 'b':4},
  'a':{'b':4},
  'b':{'a':3, 'c':2, 'd':5},
  'c':{'d':2},
  'd':{}
}
