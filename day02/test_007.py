# @Time : 2021/1/29 11:35
# @Author:曹晶晶
# 　＠File : test_007.py

'''
fixtrue：带参数
'''

import pytest


# 5组测试数据，表示不同的用户名
@pytest.fixture(params=["root", "administrator", "admin", "123456", "Test-123"])
def login_data(request):  # 固定写法
    return request.param  # 固定写法


# 2组测试数据
@pytest.fixture(params=[{"username": "root", "pwd": "1234"}, {"username": "admin", "pwd": "1234"}])
def login_data_01(request):  # 固定写法
    return request.param  # 固定写法


# 使用5组数据分别执行这个用例，共执行5次
def test_login(login_data):
    print(f"测试登录功能，使用用户名：{login_data}登录")  # format 格式化


def test_login_1(login_data_01):
    print(f"测试登录功能，用户名：{login_data_01['username']},密码为{login_data_01['pwd']}")
