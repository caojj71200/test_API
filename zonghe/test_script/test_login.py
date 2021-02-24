# @Time : 2021/2/24 9:35
# @Author:曹晶晶
# 　＠File : test_login.py
'''
注册用户（前置）
登录
检查结果
删除注册用户（后置）
'''
import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(params=(DataRead.read_yaml(r"test_data\login.yaml")))
def login(request):
    return request.param


# 前置条件
@pytest.fixture()
def register(baserequest, url, setup_data, db_info):
    # 初始化环境：避免环境中已有本次测试的数据
    MySqlOp.delete_user(setup_data['data']['mobilephone'], db_info)
    # 注册用户
    r = Member.register(baserequest, url, setup_data)
    print(r.text)
    yield  # yeild 之前是前置，之后是后置
    # 清理环境：删除用户（1.接口删除数据 2.数据库删除用户）
    MySqlOp.delete_user(setup_data['data']['mobilephone'], db_info)


def test_login(baserequest, url, register, login_data):
    # 下发登陆请求
    r = Member.login(baserequest, url, login_data['data'])
    # 检查结果
    Check.equal(r.json(),login_data['expect'],'code,status,msg')

def test_login_01(baserequest, url, login, db_info):
    # 初始化环境
    MySqlOp.delete_user(login['regdata']['mobilephone'], db_info)
    # 注册用户
    r = Member.register(baserequest, url, login['regdata'])
    print(r.text)
    r1 = Member.login(baserequest, url, login['logindata'])
    print(r1.text)
    Check.equal(r1.json(),login['expect'],'code,status,msg')

    # 清理环境
    MySqlOp.delete_user(login['logindata']['mobilephone'], db_info)



if __name__ == '__main__':
    pytest.main()
