from typing import TypeVar, Callable, List, Set, Generic, Dict, Any

T = TypeVar('T')


class Stream(Generic[T]):
    def __init__(self, list_pointer: List[T]):
        self._list_pointer = list_pointer

    def map(self, func):
        self._list_pointer = map(func, self._list_pointer)
        return self

    def filter(self, func: Callable[[Any, ...], bool]):
        self._list_pointer = filter(func, self._list_pointer)
        return self

    def for_each(self, func: Callable) -> None:
        for i in self._list_pointer:
            func(i)

    def peek(self, func: Callable):
        for i in self._list_pointer:
            func(i)
        return self

    def sorted(self):
        self._list_pointer = sorted(self._list_pointer)
        return self

    def count(self):
        return len(list(self._list_pointer))

    def to_list(self):
        return list(self._list_pointer)

    def to_set(self) -> Set:
        return set(self._list_pointer)

    def to_map(self, k: Callable, v: Callable) -> Dict:
        return {k(i): v(i) for i in self._list_pointer}
