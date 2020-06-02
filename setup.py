# coding:utf-8

from setuptools import setup
import huepy
# or
# from distutils.core import setup  

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setup(
        name='flyvar',     # 包名字
        version='1.0.6',   # 包版本
        description='A database that is convenient for version iteration',   # 简单描述
        keywords='A database that is convenient for version iteration',
        author='snbckcode',  # 作者
        author_email='snbckcode@gmail.com',  # 作者邮箱
        packages=['flyvar'],                 # 包
        install_requires=['huepy'],
        license='Mozilla',
        url='https://github.com/snbck/flyvar',
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires='>=3.6'

)

'''
皮卡丘多多(演唱)

月亮弯弯，绵绵绵绵缠缠

果汁分你一半，爱相互分担

长路慢慢，磕磕磕磕拌拌 

果汁分你一半，爱相互付缠

今晚多么美满约会相当浪漫，我果汁分你一半

我也叫你买单谁跟谁别细算，我果汁分你一半

偶尔我也会烦脸色说翻就翻，我果汁分你一半

就算怎么艰难也要保持乐观，我果汁分你一半

月亮弯弯，绵绵绵绵缠缠

果汁分你一半，爱相互分担

长路慢慢，磕磕磕磕拌拌 

果汁分你一半，爱相互扶搀

我要那个那个那个那个那个那个那个啊

你要那个那个那个那个那个那个那个啊

当喜欢上自然一个眼神交换，我果汁分你一半

我吃饭你刷碗不是我要偷懒，我果汁分你一半

偶尔你也会乱发脾气不敢惯，我果汁分你一半

向前向后攻占粘我阴魂不散，我果汁分你一半

月亮弯弯，绵绵绵绵缠缠

果汁分你一半，爱相互分担

长路慢慢，磕磕磕磕拌拌 

果汁分你一半，爱相互扶搀

我要那个那个那个那个那个那个那个啊

你要那个那个那个那个那个那个那个啊

我要那个那个那个那个那个那个那个啊

你要那个那个那个那个那个那个那个啊

月亮弯弯，绵绵绵绵缠缠

果汁分你一半，爱相互分担

长路慢慢，磕磕磕磕拌拌 

果汁分你一半，爱相互扶搀

月亮弯弯，绵绵绵绵缠缠

果汁分你一半，爱相互分担

长路慢慢，磕磕磕磕拌拌 

果汁分你一半，爱相互付缠

那那那那那那那那那那那那那那那那那那那那那

那那那那那那那那那那那那那那那那那那那那那


'''