# @Time : 2021/1/29 16:31
# @Author:曹晶晶
# 　＠File : test_011.py
'''
mock：1.接口测试时，场景不好构造出来，用Mock模拟某个人接口的返回值。
      2.依赖第三方的接口，但是接口还没有开发完成，自己接口已开发完成，没有依赖接口的环境，如何测试。

'''
from unittest import mock

import pytest
import requests


# 接口地址："https://www.zhifu.com"
# post方法
# 参数:{"订单号":12345,"支付方式":"余额宝"}字典格式
# 返回值：json {"code":1002,"msg":"支付成功"}

def zhifu(data):
    r = requests.post("https://www.zhifu.com/pay", data)
    return r.json()


def test_zhifu():
    data = {"订单号": 12345, "支付金额": 123, "支付方式": "余额宝"}
    # return_value 是参数  mock模拟场景
    zhifu = mock.Mock(return_value={"code": 1002, "msg": "支付成功"})
    r = zhifu(data)
    assert r['msg'] == '支付成功'
    print(r)


@mock.patch("test_011.zhifu", return_value={"code": 1002, "msg": "支付成功"})
def test_zhifu2(arg):
    data = {"订单号": 12345, "支付金额": 123, "支付方式": "余额宝"}
    r = zhifu(data)
    assert r['msg'] == '支付成功'


# 金融，注册用户-> 登录-> 充值1000-> 取现100 (服务器异常)
def register(data):
    url = "https://www.zhifu.com/register"
    r = requests.post(url, data)
    return r.json()


@mock.patch("test_011.register", return_value={"code": "1001", "msg": "注册成功"})
def test_01(aa):
    data = {"username": "caojingj", "pwd": "1234"}
    r = register(data)
    assert r['msg'] == '注册成功'


def login(data):
    url = "https://www.zhifu.com/login"
    r = requests.post(url, data)
    return r.json()


@mock.patch("test_011.login", return_value={"code": "1001", "msg": "登录成功"})
def test_login(aa):
    data = {"username": "caojingjing", "pwa": "12345"}
    r = login(data)
    assert r['msg'] == '登录成功'

def save_quit():
    money = 10000