# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  

setup(
        name='flyvar',     # 包名字
        version='1.0.2',   # 包版本
        description='A database that is convenient for version iteration, not bloated',   # 简单描述
        author='snbck',  # 作者
        author_email='snbckcode@gmail.com',  # 作者邮箱
        packages=['flyvar'],                 # 包
        license='Mozilla'
)