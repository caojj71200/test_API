# @Time : 2021/1/28 17:34
# @Author:曹晶晶
# 　＠File : test_login.py
import pytest
import requests

url = "http://jy001:8081/futureloan/mvc/api/member/login"


def setup():
    print("------->setup_method")


def test_login_01():
    cs = {
        "mobilephone": "",
        "pwd": ""
    }
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '手机号不能为空'
    assert rjson['code'] == '20103'


def test_login_02():
    cs = {
        "mobilephone": "13073514021",
        "pwd": ""
    }
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == "密码不能为空"
    assert rjson['code'] == '20103'


def test_login_03():
    cs = {
        "mobilephone": "",
        "pwd": "123456"
    }
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '手机号不能为空'
    assert rjson['code'] == '20103'


def test_login_04():
    cs = {
        "mobilephone": "13073514021",
        "pwd": "123456"
    }
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '登录成功'
    assert rjson['code'] == '10001'


def test_login_05():
    cs = {
        "mobilephone": "13073514021",
        "pwd": "qqqq"
    }
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '用户名或密码错误'
    assert rjson['code'] == '20111'


def test_login_06():
    cs = {
        "mobilephone": "12345678909",
        "pwd": "123456"
    }
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson['msg'] == '用户名或密码错误'
    assert rjson['code'] == '20111'


if __name__ == '__main__':
    pytest.main()
