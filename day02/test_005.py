# @Time : 2021/1/29 11:11
# @Author:曹晶晶
# 　＠File : test_005.py
import pytest


@pytest.fixture(scope='class')
def db():
    print("连接数据库")
    yield
    print("后置：类里面所有用例执行完断开数据库")


@pytest.fixture(scope='class')
def login():
    print("前置：在首次调用login的地方执行的")
    yield
    print("后置：模块中所有用例执行完之后执行，后置")


class TestRegister:
    def test_001(self):
        print("注册用例1")

    def test_002(self, db):  # 类里面首次调用db，执行前置
        print("注册用例2")

    def test_003(self):  # 类里面所有用例执行完，执行后置
        print("注册用例3")


class TestLogin:
    def test_001(self, login):  # login的前置
        print("登录用例1")

    def test_002(self, db, login):  # db的前置
        print("登录用例2")

    def test_003(self):  # login、db的后置
        print("登录用例3")
