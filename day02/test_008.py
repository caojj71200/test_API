# @Time : 2021/1/29 14:02
# @Author:曹晶晶
# 　＠File : test_008.py
import pytest

'''
有多个fixture带参数：
一个字符搜索功能，有三个输入：
要搜索字符串：大写、小写、大小写混合
搜索设置：是否区分大小写，是、否
搜索设置,搜索方向：向上搜索、向下搜索
'''


# 要搜索的字符串
@pytest.fixture(params=['HELL', "hello", "Hello"])
def zfc(request):
    return request.param


# 搜索的方向
@pytest.fixture(params=['向上', '向下'])
def fx(request):
    return request.param


# 是否区分大小写
@pytest.fixture(params=['是', '否'])
def dx(request):
    return request.param


# 3*2*2个用例
def test_search(zfc, fx, dx):
    print(f"测试搜索功能，要搜索的字符串为：{zfc},搜索的方向:{fx},是否区分大小写:{dx}")