# reduce

将列表中所有元素进行累积

## Source
```python
def reduce(self, func: Callable[[T, T], T], initial: T = None) -> Optional[T]:
    if initial:
        return reduce(func, self._stream, initial)
    else:
        try:
            return reduce(func, self._stream)
        except TypeError:
            return None
```
## Usage

将列表中每个数相加

```python
a = [1, 2, 3]
b = Stream(a).reduce(lambda x, y: x + y)
assert b == 6
c = Stream(a).reduce(lambda x, y: x + y, 10)
assert c == 16

a = []
d = Stream(a).reduce(lambda x, y: x + y)
assert d is None
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
Optional<Integer> b = a.stream()
        .reduce((x, y) -> x + y);
// b = Optional[6]

Integer c = a.stream()
        .reduce(10, (x, y) -> x + y);
// c = Optional[16]

a = Arrays.asList();
Optional<Integer> d = a.stream()
        .reduce((x, y) -> x + y);
// d = Optional.empty
```
