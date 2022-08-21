# sorted

将列表数据排序

## Source
```python
def sorted(self, key=None, reverse=False) -> 'Stream[T]':
    return Stream(sorted(self._stream, key=key, reverse=reverse))
```

## Usage

去重数据，得到新列表

```python
a = [2, 1, 3]
b = Stream(a).sorted().to_list()
assert b == [1, 2, 3]
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3, 3);
List<Integer> b = a.stream()
        .distinct()
        .collect(Collectors.toList());
```

## Advanced

去重数据，得到新列表，并反转

```python
a = [2, 1, 3]
b = Stream(a).sorted(reverse=True).to_list()
assert b == [3, 2, 1]
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(2, 1, 3);
List<Integer> b = a.stream()
        .sorted((x, y) -> y - x)
        .collect(Collectors.toList());
```
