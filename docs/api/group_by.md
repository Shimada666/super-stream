# map

将列表中元素按指定规则分类

## Source

## Usage

将列表中每个元素按 name 属性归类

```python
a = [{'age': 18, 'name': 'foo'}, {'age': 18, 'name': 'bar'}, {'age': 28, 'name': 'bar'}]
b = Stream(a).group_by(lambda x: x['name'])
# b = {'foo': [{'age': 18, 'name': 'foo'}], 'bar': [{'age': 18, 'name': 'bar'}, {'age': 28, 'name': 'bar'}]}
```

等价的 java 代码
```java
@Data
@AllArgsConstructor
class Person {
    private int age;
    private String name;
}

List<Person> a = Arrays.asList(new Person(18, "foo"), new Person(18, "bar"), new Person(28, "bar"));
Map<String, List<Person>> b = a.stream()
        .collect(Collectors.groupingBy(Person::getName));
```

## Advanced