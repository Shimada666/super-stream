# Python Stream

[![Test](https://github.com/Shimada666/python-stream/actions/workflows/main.yml/badge.svg)](https://github.com/Shimada666/python-stream/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Shimada666/python-stream/branch/master/graph/badge.svg)](https://codecov.io/gh/Shimada666/python-stream)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

在用使用过 Typescript 与 Java 方便的链式调用后，回到 Python 再想实现同样的功能  
高阶函数的套娃让你很痛苦吧？  
性能开销都在其次，主要是写着蛋疼啊！

现在一个轻量级流式处理工具来了，利用 python 内置特性，他可以轻松实现

* 更高的可读性
* 惰性求值（无论中途map，filter多少次，数据只在最后遍历一次）
* 完善的类型提示，即使你使用 lambda

### 安装

直接复制 stream.py 里的代码，将来完善后上 pypi 可以使用 pip 安装，但现在还不支持

### 使用

### 与 java stream 的对照

* 暂不支持并行 parallel
* 大部分功能已支持，行为相同

#### 主要方法支持列表
- [x] map
- [x] forEach
- [x] filter
- [x] reduce
- [x] sorted
- [x] limit
- [x] skip
- [x] count
- [x] distinct
- [ ] flatMap 正在施工中
- [x] findAny/findFirst
- [x] anyMatch/allMatch/noneMatch

|  Java Stream  | Python Stream   |     备注      |
|---------------|-----------------|-----------|
|    filter     |     filter      |           |
|    map     |     map      |   |           |
|    mapToInt       |     -      |           |
|    mapToLong       |     -      |           |
|    mapToDouble       |     -      |           |
|    flatMap       |     -      |           |
|    flatMapToInt       |     -      |           |
|    flatMapToLong       |     -      |           |
|    flatMapToDouble       |     -      |           |
|    distinct       |     distinct      |           |
|    sorted       |     sorted      |           |
|    peek       |      -      |    peek 在 java stream 多为调试功能， python stream 将不会实现，可用 map 并返回元素本身代替       |
|    limit       |     limit      |           |
|    skip       |     skip      |           |
|    forEach       |     for_each      |           |
|    reduce       |     reduce      |           |
|    count       |     count      |           |
|    min       |     -      |           |
|    max       |     -      |           |
|    findAny       |     find_first      |      findAny 可用 findFirst 代替     |
|    findFirst       |     find_first      |           |
|    anyMatch       |     any_match      |           |
|    noneMatch       |     none_match      |           |
|    allMatch       |     all_match      |           |
|    iterate       |     -      |    不常用，不会提供     |
|    generate       |     -      |   不常用，不会提供        |
|    concat       |     -      |    不常用，不会提供        |

### FAQ
