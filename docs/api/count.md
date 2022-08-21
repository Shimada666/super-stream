# count

获得列表长度

## Source

## Usage

获得当前列表长度

```python
a = [1, 2, 3]
b = Stream(a).count()
assert b == 3
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
long b = a.stream().count();
```
