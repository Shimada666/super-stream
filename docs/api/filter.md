# filter

将列表中数据按条件过滤

## Usage

过滤出列表中大于 1 的数

```python
a = [1, 2, 3]
b = Stream(a).filter(lambda x: x > 1).to_list()
```

等价的 java 代码
```java
List<Integer> ints = Arrays.asList(1, 2, 3);
List<Integer> doubleInts = ints.stream()
        .map(i -> i > 1)
        .collect(Collectors.toList());
```