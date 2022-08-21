# any_match111222444

判断列表中是否所有元素都匹配上给定的条件

## Source
```python
def all_match(self, func: Callable[[T], bool]) -> bool:
    return all(map(func, self._stream))
```
## Usage

判断列表中是否元素均小于 4

```python
a = [1, 2, 3]
b = Stream(a).all_match(lambda x: x < 4)
assert b is True
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
boolean b = a.stream()
        .allMatch(x -> x < 4);
```
