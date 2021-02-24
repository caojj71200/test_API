# @Time : 2021/1/29 11:20
# @Author:曹晶晶
# 　＠File : conftest.py
'''
    session级别的前置和后置，放到conftest.py文件中
    不需要import，pytest根据文件名字对应的方法
    脚本层的一些公共方法，可以放到这里
    一个工程可以包含多个conftest.py，conftest对同级目录以及该目录下的子目录生效
    作用域：在当前目录下，以及当前目录的子目录
'''
import pytest


@pytest.fixture(scope='session')
def db():
    print("连接数据库")
    yield
    print("后置：类里面所有用例执行完断开数据库")


@pytest.fixture(scope='session')
def login():
    print("前置：整个执行过程，在首次调用login的地方执行前置")
    yield
    print("后置：整个执行过程中所有用例执行完之后执行后置")
