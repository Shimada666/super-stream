from typing import TypeVar, Callable, List, Set, Generic, Dict, Iterator

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K')
U = TypeVar('U')


class Stream(Generic[T]):
    def __init__(self, stream: Iterator[T] = None):
        if stream:
            self._stream = stream
        else:
            self._stream = iter([])

    def map(self, func: Callable[[T], R]) -> 'Stream'[R]:
        return Stream(map(func, self._stream))

    def filter(self, func: Callable[[T], bool]) -> 'Stream'[T]:
        return Stream(filter(func, self._stream))

    def for_each(self, func: Callable[[T], None]) -> None:
        for i in self._stream:
            func(i)

    def peek(self, func: Callable[[T], None]) -> 'Stream'[T]:
        for i in self._stream:
            func(i)
        return self

    def sorted(self) -> 'Stream'[T]:
        return Stream(sorted(self._stream))

    def count(self) -> int:
        return len(list(self._stream))

    def to_list(self) -> List[T]:
        return list(self._stream)

    def to_set(self) -> Set[T]:
        return set(self._stream)

    def to_map(self, k: Callable[[T], K], v: Callable[[T], U]) -> Dict[K, U]:
        return {k(i): v(i) for i in self._stream}
