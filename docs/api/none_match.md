# none_match

判断列表中是否没有任何元素能够匹配上给定的条件

## Source
```python
def none_match(self, func: Callable[[T], bool]) -> bool:
    return not self.any_match(func)
```
## Usage

判断列表中是否存在小于 0 的元素

```python
a = [1, 2, 3]
b = Stream(a).none_match(lambda x: x < 0)
assert b is True
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
boolean b = a.stream()
        .noneMatch(x -> x < 0);
```
