# linked list

from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
  data: Any
  nextNode: Any

@dataclass
class LinkedList:
  head: Any
  tail: list[Any]