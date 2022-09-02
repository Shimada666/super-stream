from functools import reduce
from typing import TypeVar, Callable, List, Set, Generic, Dict, Iterable, Optional, Any
from itertools import islice, chain

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K')
U = TypeVar('U')


class Stream(Generic[T]):
    def __init__(self, stream: Iterable[T]):
        self._stream = iter(stream)

    def __iter__(self):
        return self._stream

    @staticmethod
    def of(*args: T) -> 'Stream[T]':
        return Stream(args)

    def map(self, func: Callable[[T], R]) -> 'Stream[R]':
        return Stream(map(func, self._stream))

    def flat_map(self, func: Callable[[T], 'Stream[R]']) -> 'Stream[R]':
        return Stream(chain.from_iterable(map(func, self._stream)))

    def filter(self, func: Callable[[T], bool]) -> 'Stream[T]':
        return Stream(filter(func, self._stream))

    def for_each(self, func: Callable[[T], None]) -> None:
        for i in self._stream:
            func(i)

    def distinct(self):
        return Stream(list(dict.fromkeys(self._stream)))

    def sorted(self, key=None, reverse=False) -> 'Stream[T]':
        return Stream(sorted(self._stream, key=key, reverse=reverse))

    def count(self) -> int:
        return len(list(self._stream))

    def sum(self) -> 'T':
        return sum(self._stream)

    def group_by(self, classifier: Callable[[T], K]) -> Dict[K, List[T]]:
        groups = {}
        for i in self._stream:
            groups.setdefault(classifier(i), []).append(i)
        return groups

    def reduce(self, func: Callable[[T, T], T], initial: T = None) -> Optional[T]:
        if initial is not None:
            return reduce(func, self._stream, initial)
        else:
            try:
                return reduce(func, self._stream)
            except TypeError:
                return None

    def limit(self, max_size: int) -> 'Stream[T]':
        return Stream(islice(self._stream, max_size))

    def skip(self, n: int) -> 'Stream[T]':
        return Stream(islice(self._stream, n, None))

    def min(self, key: Callable[[T], Any] = None, default: T = None) -> T:
        """
        :param default: use default value when stream is empty
        :param key: at lease supported __lt__ method
        """
        if key is not None:
            return min(self._stream, key=key, default=default)
        return min(self._stream)

    def max(self, key: Callable[[T], Any] = None, default: T = None) -> T:
        """
        :param default: use default value when stream is empty
        :param key: at lease supported __lt__ method
        """
        if key is not None:
            return max(self._stream, key=key, default=default)
        return max(self._stream)

    def find_first(self) -> Optional[T]:
        try:
            return next(self._stream)
        except StopIteration:
            return None

    def any_match(self, func: Callable[[T], bool]) -> bool:
        """
        this is equivalent to
            for i in self._stream:
                if func(i):
                    return True
            return False
        :param func:
        :return:
        """
        return any(map(func, self._stream))

    def all_match(self, func: Callable[[T], bool]) -> bool:
        return all(map(func, self._stream))

    def none_match(self, func: Callable[[T], bool]) -> bool:
        return not self.any_match(func)

    def to_list(self) -> List[T]:
        return list(self._stream)

    def to_set(self) -> Set[T]:
        return set(self._stream)

    def to_map(self, k: Callable[[T], K], v: Callable[[T], U]) -> Dict[K, U]:
        return {k(i): v(i) for i in self._stream}