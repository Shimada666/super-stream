# map

将列表中所有元素统一进行操作，如将每个数乘 2

## Usage

将列表中每个数乘以 2

```python
a = [1, 2, 3]
b = Stream(a).map(lambda x: x * 2).to_list()
```

等价的 java 代码
```java
List<Integer> ints = Arrays.asList(1, 2, 3);
List<Integer> doubleInts = ints.stream()
        .map(i -> i * 2)
        .collect(Collectors.toList());
```

## Advanced
