# any_match

判断列表中是否有任何一个元素匹配上给定的条件

## Source
```python
def any_match(self, func: Callable[[T], bool]) -> bool:
    return any(map(func, self._stream))
```
## Usage

判断列表中是否有小于 2 的元素

```python
a = [1, 2, 3]
b = Stream(a).any_match(lambda x: x < 2)
assert b is True
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
boolean b = a.stream()
        .anyMatch(x -> x < 2);
```
