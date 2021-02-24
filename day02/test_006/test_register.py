# @Time : 2021/1/29 11:24
# @Author:曹晶晶
# 　＠File : test_register.py

class TestRegister:
    def test_001(self):
        print("注册用例1")

    def test_002(self, db):  # 类里面首次调用db，执行前置
        print("注册用例2")

    def test_003(self):  # 类里面所有用例执行完，执行后置
        print("注册用例3")
