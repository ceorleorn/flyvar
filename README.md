# 前言
#### 你可能厌倦了PyMsql的枯燥，那就看看Flyvar吧.他不臃肿，简易.适合帮助中小型项目存储数据
# 安装
#### Flyvar的大小可能出乎你的，他的源码只有12K左右。并且没有依赖超过三个需要安装的库.
#### 在Pip安装
`pip install flyvar`
# 服务端
#### Flyvar与Mysql一样，服务端与客户端隔离。需要客户端通过连接服务器来操作数据，当然也可以把服务端放在与客户端在一个主机上！
## Server类
```python
import flyvar
db = flyvar.Server()
```
#### Server类是