# for_each

将列表中所有元素依次进行操作，无返回值，stream 到这里就会停止。

## Usage

将列表中数据依次打印

```python
a = [1, 2, 3]
Stream(a).for_each(lambda x: print(x))
```

等价的 java 代码
```java
List<Integer> a = Arrays.asList(1,2,3);
a.stream()
        .forEach(System.out::println);
```