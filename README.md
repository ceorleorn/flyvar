# 前言
#### 你可能厌倦了PyMysql的枯燥，那就看看Flyvar吧.他不臃肿，简易.基于Python3构建
# 安装
#### Flyvar的大小可能出乎你的，他的源码只有12K左右。并且没有依赖超过三个需要安装的库.
#### 在Pip安装
`pip install flyvar`
# 服务端
#### Flyvar与Mysql一样，需要服务端和客户端。需要客户端通过连接服务器来操作数据，当然也可以把服务端放在与客户端在一个主机上！
## Server类
```python
import flyvar
db = flyvar.Server(host='127.0.0.1',port=18012)
```
#### Server类是整个服务端的对象，他可以帮助服务端运行和处理事务.可以在赋值时指定运行的端口
## Server.run()
```python
import flyvar
db = flyvar.Server()
db.Run()
```
#### Server.run()方法将数据库在端口运行，此时会在子目录下创建 "Flying"文件夹，利用里面的存储的数据库运行，不过目前是空的.
## Server.CreateDataBase()
```python
import flyvar
db = flyvar.Server(host='127.0.0.1',port=18012)
db.CreateDataBase('testdatabase','testuser','password')
```
#### 此时可以看到在目录 "/Flying"中新建了文件夹testdatabase，文件夹中包括文件"__init__.flying"，次=此文件声明了数据库的最最基本信息，但数据库还是空的.

# 客户端
### Flyvar的客户端很简单，不臃肿
## Database类
```python
import flyvar
database = flyvar.Database()
```
#### 我们赋值了一个Database对象，让我们用他链接到服务器
## Database.connect()
```python
import flyvar
database = flyvar.Database()
database.connect(
    host='127.0.0.1',
    port=18012,
    name='testdatabase',
    user='testuser',
    password='password'
)
```
#### 我们成功连接上了刚刚的服务端，并初始化了Database对象，输出如下:
```Bash
[+] Welcome use Flyvar
[~] Successfully connected
[+] Downloaded identity certificate:ecc4ba55675b0dd7586171fcea38685ea838b98b64bcbb9b2625bc1be5284bab
```
## 问题排查
```Bash
[+] Welcome use Flyvar
[-] Connection failed, please check the network or address
```
#### 网络错误，建议检查端口和地址是否正确，或者重复连接
```Bash
[+] Welcome use Flyvar
[~] Successfully connected
[-] Connection failed, please check the address or databasename
```
#### 404，建议检查数据库名是否正确，或者没有在服务端创建
```Bash
[+] Welcome use Flyvar
[~] Successfully connected
[-] Connection failed, please check the username or password
```
#### 权限错误，建议检查用户名和密码
