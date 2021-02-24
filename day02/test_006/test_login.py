# @Time : 2021/1/29 11:24
# @Author:曹晶晶
#　＠File : test_login.py
class TestLogin:
    def test_001(self, login):  # login的前置
        print("登录用例1")

    def test_002(self, db, login):  # db的前置
        print("登录用例2")

    def test_003(self):  # login、db的后置
        print("登录用例3")
