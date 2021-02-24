# @Time : 2021/1/29 14:19
# @Author:曹晶晶
# 　＠File : test_009.py

'''
fixture 嵌套
'''
import random
import pytest
import requests


# 生成用户名
@pytest.fixture()
def get_username():
    return "admin" + str(random.randint(1, 1000))


# 生成密码
@pytest.fixture()
def get_password():
    return random.randint(100000, 999999)


@pytest.fixture()
def get_login_data(get_username, get_password):
    return {"username": get_username, "pass": get_password}


# 测试用例
def test_login(get_login_data):
    print(f"测试登陆功能,登录的数据为：{get_login_data}")


# 练习：用fixture+requests,优化金融项目注册的接口脚本

cs = [
    {"data": {"mobilephone": "", "pwd": ""}, "expect": {'status': 0, 'code': '20103', 'data': None, 'msg': '手机号不能为空'}},
    {"data": {"mobilephone": "123456789", "pwd": ""},
     "expect": {'status': 0, 'code': '20103', 'data': None, 'msg': '密码不能为空'}},
    {"data": {"mobilephone": "123456789", "pwd": "12345"},
     "expect": {'status': 0, 'code': '20108', 'data': None, 'msg': '密码长度必须为6~18'}},
    {"data": {"mobilephone": "1234567890", "pwd": "123456"},
     "expect": {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}},
    {"data": {"mobilephone": "12345678", "pwd": "123456789012345678"},
     "expect": {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}},
    {"data": {"mobilephone": "1845676",
              "pwd": "1234567890123456789", },
     "expect": {'status': 0, 'code': '20108', 'data': None, 'msg': '密码长度必须为6~18'}},
    {"data": {"mobilephone": "18456765457",
              "pwd": "", }, "expect": {'status': 0, 'code': '20103', 'data': None, 'msg': '密码不能为空'}},
]


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.get(url, params=data)
    return r


@pytest.fixture(params=cs)
def get_register_data(request):
    return request.param


# 数据驱动的测试模型，
# test_register_001 测试脚本/测试逻辑，测试数据与测试逻辑分离，相同逻辑的数据放在一起，实现一个脚本
# 数据可以放到 CSV、yaml、Excel、xml
def test_register_001(get_register_data):
    print(f"测试数据：{get_register_data['data']}")
    print(f"测试结果:{get_register_data['expect']}")
    r = register(get_register_data['data'])
    assert r.json() == get_register_data['expect']
