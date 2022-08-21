# find_first

获得列表中第一个元素

## Source
```python
def find_first(self) -> Optional[T]:
    try:
        return next(self._stream)
    except StopIteration:
        return None
```
## Usage

获得列表中第一个元素

```python
a = [1, 2, 3]
b = Stream(a).find_first()
assert b == 1

a = []
b = Stream(a).find_first()
assert b is None
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
Optional<Integer> b = a.stream()
        .findFirst();

a = Arrays.asList();
b = a.stream()
        .findFirst();
```
