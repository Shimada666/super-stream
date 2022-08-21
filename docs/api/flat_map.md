# flat_map

将列表数据按需展平，组成一个新的列表

## Usage

存在一个二维列表，里面每一项都是一个列表，希望将其展平，获得一维列表

```python
a = [[1, 2, 3], [4, 5, 6]]
b = Stream(a).flat_map(lambda x: Stream(x)).to_list()
assert b == [1, 2, 3, 4, 5, 6]
```

等价的 java 代码
```java
List<List<Integer>> a = Arrays.asList(Arrays.asList(1,2,3), Arrays.asList(4,5,6));
List<Integer> b = a.stream()
        .flatMap(Collection::stream)
        .collect(Collectors.toList());
```