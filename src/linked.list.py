# linked list

from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
  data: Any = None
  next: Any = None

@dataclass
class LinkedList:
  head: Any = None
  tail: list[Any] = list()