# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setup(
        name='flyvar',     # 包名字
        version='1.0.5',   # 包版本
        description='A database that is convenient for version iteration',   # 简单描述
        keywords='A database that is convenient for version iteration',
        author='snbckcode',  # 作者
        author_email='snbckcode@gmail.com',  # 作者邮箱
        packages=['flyvar','huepy'],                 # 包
        license='Mozilla',
        url='https://github.com/snbck/flyvar',
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires='>=3.6'

)