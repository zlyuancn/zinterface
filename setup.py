#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='zinterface',
    version='0.1.0',
    py_modules=['zinterface'],
    author='zlyuan',
    author_email='zlyuancn@163.com',
    packages=find_packages(),
    description='python的interface模式',
    long_description=open('README.md', 'r', encoding='utf8').read(),  # 项目介绍
    long_description_content_type='text/markdown',
    url='https://github.com/zlyuancn/zinterface',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts=[],  # 额外的文件
    install_requires=[],  # 依赖库
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
