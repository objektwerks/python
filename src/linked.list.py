# linked list

from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")

@dataclass
class Node(Protocol[T]):
  data: T
  next: T

@dataclass
class LinkedList(Protocol[T]):
  head: T
  tail: list[T]