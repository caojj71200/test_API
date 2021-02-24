# @Time : 2021/1/28 16:43
# @Author:曹晶晶
# 　＠File : test_register.py

'''
1.文件名以test_开头
2.类名用Test开头
3.函数名或方法以test_开头
'''

import requests
import pytest

url = "http://jy001:8081/futureloan/mvc/api/member/register"


def test_register_001():  # 手机号为空，密码为空
    cs = {
        "mobilephone": "",
        "pwd": "",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['code'] == '20103'
    assert rjson['msg'] == '手机号不能为空'


def test_register_002():  # 手机号码小于11位，密码为空
    cs = {
        "mobilephone": "123456789",
        "pwd": "",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '密码不能为空'
    assert rjson['code'] == '20103'


def test_register_003():  # 手机号码小于11位，密码不为空小于6位
    cs = {
        "mobilephone": "123456789",
        "pwd": "12345",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '密码长度必须为6~18'
    assert rjson['code'] == "20108"


def test_register_004():  # 手机号码小于11位，密码为位6位
    cs = {
        "mobilephone": "1234567890",
        "pwd": "123456",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '手机号码格式不正确'
    assert rjson['code'] == "20109"


def test_register_005():  # 手机号码小于11位，密码为空位于18位
    cs = {
        "mobilephone": "12345678",
        "pwd": "123456789012345678",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '手机号码格式不正确'
    assert rjson['code'] == "20109"


def test_register_006():  # 手机号码小于11位，密码为空位于19位
    cs = {
        "mobilephone": "1845676",
        "pwd": "1234567890123456789",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '密码长度必须为6~18'
    assert rjson['code'] == '20108'


def test_register_007():  # 手机位11位，密码为空
    cs = {
        "mobilephone": "18456765457",
        "pwd": "",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '密码不能为空'
    assert rjson['code'] == '20103'


def test_register_008():  # 手机号为11位，密码为6位
    cs = {
        "mobilephone": "12345678909",
        "pwd": "123456",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '手机号码格式不正确'
    assert rjson['code'] == '20109'


def test_register_009():  # 手机号码为11位，密码为18位
    cs = {
        "mobilephone": "18456765424",
        "pwd": "123456789009876543",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '注册成功'
    assert rjson['code'] == '10001'


def test_register_010():  # 手机号码为11位，密码为19位
    cs = {
        "mobilephone": "18456765497",
        "pwd": "1234567890987654321",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '密码长度必须为6~18'
    assert rjson['code'] == '20108'


def test_register_0011():  # 手机号为空，密码为5位
    cs = {
        "mobilephone": "",
        "pwd": "12345",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '手机号不能为空'
    assert rjson['code'] == '20103'


def test_register_0012():  # 手机号为1789014567809，密码为空
    cs = {
        "mobilephone": "1789014567809",
        "pwd": "",
        "regname": ""
    }
    r = requests.get(url, params=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '密码不能为空'
    assert rjson['code'] == '20103'


if __name__ == '__main__':
    pytest.main()
