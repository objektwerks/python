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
  tail: list[T] = list[T]()

  def of(self, items: list[T]) -> None:
    len: int = len(items)
    if len > 0:
      head = items[0]
      if len > 1:
        tail = list[T][1:len - 1]
    else:
      raise Exception("LinkedList requires at least 1 item.")

data: LinkedList[int] = LinkedList(1, [2, 3])