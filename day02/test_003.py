# @Time : 2021/1/29 10:20
# @Author:曹晶晶
# 　＠File : test_003.py

'''
更灵活的一种前置后置
    可以不需要setup teardown方法名，使用起来更加灵活
    fixture:1.通过参数引用
            2.通过装饰引用@pytest.mark.usefixtures()
            3.fixture：带参数 固定写法：参数是列表，获取参数:request.param
            4.多个fixture带参数，测试用例为全排列
            5.fixture嵌套
    fixture级别：
        session、class、module、function（默认为function）
        session级别的前置和后置，放到conftest.py文件中
            不需要import，pytest根据文件名字对应的方法
            脚本层的一些公共方法，可以放到这里
            一个工程可以包含多个conftest.py，conftest对同级目录以及该目录下的子目录生效
            作用域：在当前目录下，以及当前目录的子目录
'''

import pytest

''' 
测试前置：测试之前的环境准备、环境初始化、测试数据准备等
测试后置：测试结束后的环境恢复
'''


@pytest.fixture(scope='function')  # fixture作用域默认是function级别的
def login():
    print("登录，测试前置") 
    yield  # yield之前是前置，yield之后是后置
    print("退出系统")
    print("测试结束")


def test_query():
    print("查询功能，不需要登录")


def test_add(login):
    print("添加功能，需要登录")


@pytest.mark.usefixtures('login')
def test_dele(login):
    print("删除功能，需要登录")


def test_register():
    print("注册功能，不需要登录")


if __name__ == '__main__':
    pytest.main()
