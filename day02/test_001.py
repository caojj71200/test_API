# @Time : 2021/1/29 10:02
# @Author:曹晶晶
# 　＠File : test_001.py

'''测试前置和后置
    模块级和函数级
    名字不能写错，pytest根据名字来识别前置和后置
'''

import pytest


def setup_module():
    print("前置模块，模块中所有用例前执行一次")


def teardown_module():
    print("后置模块，模块中所有用例后执行一次")


def setup_function():
    print("前置模块，模块中每个用例前执行一次")


def teardown_function():
    print("后置模块，模块中每个用例后执行一次")


def test_001():
    print("测试用例1")


def test_002():
    print("测试用例2")


def test_003():
    print("测试用例3")


if __name__ == '__main__':
    pytest.main()
