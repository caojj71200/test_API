# @Time : 2021/2/23 14:12
# @Author:曹晶晶
# 　＠File : test_register.py
'''注册脚本'''
import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check

# 参数
from zonghe.test_script.conftest import baserequest, url


@pytest.fixture(params=DataRead.read_yaml(r"test_data\register_fail.yaml"))
def fail_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml(r"test_data\rejster_success.yaml"))
def sucess_data(request):
    return request.param


# 注意带参数的测试用例,conftest配置文件实现前置应用
def test_register_fail(fail_data, baserequest, url):
    '''
    :return:
    '''
    # 下发请求
    # 检查结果与预期结果一致
    print(fail_data)
    r = Member.register(baserequest, url, fail_data['data'])
    print(r.text)
    Check.equal(r.json(),fail_data['expect'],'code,status,msg')
    # assert r.json()['code'] == fail_data['expect']['code']



def test_register_pass(sucess_data, baserequest, url, db_info):
    '''
     注册成功
    :return:
    '''
    # 初始化
    MySqlOp.delete_user(sucess_data['data']['mobilephone'], db_info)
    # 下发请求
    r = Member.register(baserequest, url, sucess_data['data'])
    print(r.text)
    # 检查接口返回与预期结果一致
    assert r.json()['msg'] == sucess_data['expect']['msg']
    assert r.json()['code'] == sucess_data['expect']['code']
    assert r.json()['status'] == sucess_data['expect']['status']
    # 检查用户在系统中注册成功
    r1 = Member.list(baserequest, url)
    assert sucess_data['data']['mobilephone'] in r1.text
    # 清理环境,删除用户
    # MySqlOp.delete_user(sucess_data['data']['mobilephone'],db_info)
    # 测试原则：测试环境，在执行脚本前是什么状态，执行完脚本之后恢复到之前的状态（清理环境）
    # 脚本执行依赖的环境，要在脚本中自己构造，
    # 审核项目接口测试时依赖已有的项目，需要先调用添加项目的接口准备测试环境
    # 脚本的健壮性，稳定性比较高

    # 重负注册测试逻辑
    # 环境准备：下发注册请求
    # 测试步骤：测试下发注册请求（检查结果，报错重复注册）
    # 恢复环境：删除用户


def test_register_repeat(baserequest, url, sucess_data, db_info):

    # 环境准备
    MySqlOp.delete_user(sucess_data['data']['mobilephone'], db_info)
    Member.register(baserequest, url, sucess_data['data'])
    # 测试步骤：测试下发注册请求（检查结果，报错重复注册）
    r1 = Member.register(baserequest, url, sucess_data['data'])
    print(r1.text)
    # 恢复环境
    MySqlOp.delete_user(sucess_data['data']['mobilephone'], db_info)


if __name__ == '__main__':
    pytest.main()
