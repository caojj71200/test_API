# @Time : 2021/1/28 19:37
# @Author:曹晶晶
# 　＠File : test_01.py
'''
pytest : 类名以Test开头，文件名/包名：以test_开头，测试用例：以test_开头
执行 ：pytest 文件路径／测试文件名 ，否则会执行所有以test开头的方法

Exit code 0 所有用例执行完毕，全部通过
Exit code 1 所有用例执行完毕，存在Failed的测试用例
Exit code 2 用户中断了测试的执行
Exit code 3 测试执行过程发生了内部错误
Exit code 4 pytest 命令行使用错误
Exit code 5 未采集到可用测试用例文件

命令行执行指定用例：pytest test_register.py::test_register_0012 注意是由 ::

rerunfailures 重新执行失败的用例
pytest 是多种运行模式 -n 4

setup 执行测试用例之前运行，执行一次测试用例，就运行一次
tearDown 测试用例之后运行

setup_class 只执行一次在测试用例之前
teardown_class 只执行一次在用例之后

@pytest.fixture：执行优先

skipif 跳过指定测试用例
'''

import pytest


@pytest.fixture(autouse=True)
def befor():
    print("参数")


def test_01():
    print("测试")
