# sum

对列表进行求和

## Usage

对列表进行求和

```python
a = [1, 2, 3]
b = Stream(a).sum()
assert b == 6
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1, 2, 3);
int b = a.stream()
        .mapToInt(x -> x)
        .sum();
```
