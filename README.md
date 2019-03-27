# SFZ

A simple Package to deal with Mainland ID Card Number.
一个用来处理大陆身份证号码的小包。

# 用法

先安装啦~

```bash
pip3 install sfz
```
然后引入这个包：

```python
from sfz import *
```

## 获得户籍归属地

正常情况下会返回地址，否则返回 "Unknown"。

```python
>>> s = "432503197505028819"
>>> object = Sfz(s)                                                  
>>> object.loc()
'湖南省娄底地区涟源市'
```

## 获得性别

```python
>>> object.gender()
'男'
```

地址列表來自：[https://gist.github.com/mayufo/4207ed3fa925e6b3df7559832af85165](https://gist.github.com/mayufo/4207ed3fa925e6b3df7559832af85165)。
