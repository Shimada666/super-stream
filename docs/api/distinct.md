# distinct

将列表中数据去重

## Usage

去重数据，得到新列表

```python
a = [1, 2, 3, 3]
b = Stream(a).distinct().to_list()
assert b == [1, 2, 3]
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3, 3);
List<Integer> b = a.stream()
        .distinct()
        .collect(Collectors.toList());
```