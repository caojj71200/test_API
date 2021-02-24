# @Time : 2021/1/29 15:44
# @Author:曹晶晶
# 　＠File : test_010.py
'''
自定义标记：
    1.  跳过测试用例：这个版本有缺陷，导致用例执行失败，缺陷修改时间长，自动化通过率有一定的要求
        为了不影响通过率，可以将失败的用例跳过，待缺陷解决后，在执行
        @pytest.mark.skip用例跳过
    2. 某个功能在最新版本VR2实现的，在VR2之前的版本都不执行
        skipif(Vesrion == 'VR2', reason="非VR2版本不支持") 有条件的跳过
    执行某一部分用例：界面、接口、功能、冒烟规模逐步增大，只想执行冒烟测试的用例，
    或者只执行接口的用例，可以用自定义标记（mark之后）
    smoke 冒烟用例
    func 功能用例
    Opi 接口用例

'''
import pytest

Vesrion = 'VR2'

@pytest.mark.smoke
@pytest.mark.smoke
def test_001():
    print("用例1")


@pytest.mark.skip('跳过的原因：由于XXXX缺陷导致，该缺陷近期解决不了')
def test_002():
    print("用例2")


# skipif 第一个参数是一个把表达式，结果为true时，跳过，false执行
@pytest.mark.skipif(Vesrion == 'VR2', reason="非VR2版本不支持")
def test_003():
    print("用例3")


@pytest.mark.func
class TestMark:
    def test_004(self):
        print("用例4")

    @pytest.mark.smoke
    def test_005(self):
        print("用例5")

    def test_006(self):
        print("用例6")

    def test_007(self):
        print("用例7")

    def test_008(self):
        print("用例8")
