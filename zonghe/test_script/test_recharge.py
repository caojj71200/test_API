# @Time : 2021/2/24 11:23
# @Author:曹晶晶
# 　＠File : test_recharge.py
from unittest import mock

import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


@pytest.fixture(params=DataRead.read_yaml(r'test_data\recharge_data.yaml'))
def recharge_data(request):
    return request.param


@pytest.fixture()
def register_login(baserequest, url, recharge_data, db_info):
    # 初始化环境
    MySqlOp.delete_user(recharge_data['regdata']['mobilephone'], db_info)
    # 注册用户
    Member.register(baserequest, url, recharge_data['regdata'])
    # 用户登录
    Member.login(baserequest, url, recharge_data['logindata'])
    yield
    MySqlOp.delete_user(recharge_data['regdata']['mobilephone'], db_info)


def test_recharge(baserequest, url, register_login, recharge_data):
    r = Member.recharge(baserequest, url, recharge_data['recdata'])
    print(r.text)
    Check.equal(r.json(), recharge_data['expect'], 'status,code,msg')
