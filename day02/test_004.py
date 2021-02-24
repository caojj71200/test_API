# @Time : 2021/1/29 10:34
# @Author:曹晶晶
# 　＠File : test_004.py
import pytest

'''
fixture级别：
    session、class、module、function（默认为function）
'''


@pytest.fixture(scope='module')
def db():
    print("连接数据库")
    yield
    print("后置：断开数据库")


@pytest.fixture(scope='module')
def login():
    print("前置：在首次调用login的地方执行的")
    yield
    print("后置：模块中所有用例执行完之后执行，后置")


def test_01():
    print("用例1")


def test_02(login,db):  # 这个用例前执行前置
    print("用例2")


def test_013():  # 这个用例之后执行后置
    print("用例3")
