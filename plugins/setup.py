#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "SongUtils",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ["pip", "SongUtils"],			# 关键字
    description = "Junjie's private utils.",	# 描述
    long_description = "Junjie's private utils.",
    license = "MIT Licence",		# 许可证

    url = "https://github.com/Adenialzz/SongUtils",     #项目相关文件地址，一般是github项目地址即可
    author = "Adenialzz",			# 作者
    author_email = "********@***.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy", "pillow"]          #这个项目依赖的第三方库
)
