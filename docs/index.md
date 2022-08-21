---
layout: home

hero:
  name: SuperStream
  text: 轻量级流式处理工具
  tagline: 复刻 Java Stream API。拥有高可读性、惰性求值、类型提示等特性，帮您更轻松地处理列表
  image:
    src: /logo.png
    alt: VitePress
  actions:
    - theme: brand
      text: Get Started
      link: /api/map
    - theme: alt
      text: View on GitHub
      link: https://github.com/shimada666/super-stream
features:
- title: 高可读性
  details: 相比于 Python 原生的列表推导式、map/filter 等高阶函数套娃, SuperStream 能让你用流式 API 更清晰的处理代码。
- title: 惰性求值
  details: 无论写多少个 map、filter 改变列表，最终只遍历一次。得益于 python 自身特性，让我们能很简单地实现惰性求值。
- title: 类型提示
  details: 无论是高阶函数套娃，还是传统的流式处理库使用管道符进行链接，在类型提示上都做的不好。使用 SuperStream, 能够轻松地拥有类型提示。
---
