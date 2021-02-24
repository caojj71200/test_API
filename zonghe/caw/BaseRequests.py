# @Time : 2021/2/23 11:36
# @Author:曹晶晶
# 　＠File : BaseRequests.py
'''
1.get post 方法做异常处理
2.打印日志
3.保持会话使用session，使用session发送请求
'''
import requests

class BaseRequests:

    def __init__(self):
        # 创建session
        self.session = requests.session()

    def get(self, url, **kwargs):
        try:
            r = self.session.get(url, **kwargs)
            # f 格式化
            print(f"发送get请求，url:{url},请求参数{kwargs}成功。")
            return r
        except Exception as e:
            print(f"发送get请求，url:{url},请求参数{kwargs}成功。")

    def post(self, url, **kwargs):
        try:
            r = self.session.post(url, **kwargs)
            # f 格式化
            print(f"发送post请求，url:{url},请求参数{kwargs}成功。")
            return r
        except Exception as e:
            print(f"发送post请求，url:{url},请求参数{kwargs}成功。")


if __name__ == '__main__':
    r = BaseRequests().get("http://192.168.1.64:8089/futureloan/mvc/api/member/list")
    print(r.text)
    r = BaseRequests().post("http://192.168.1.64:8089/futureloan/mvc/api/member/login",
                            data={"mobilephone": "", "pwd": "123456"})
    print(r.text)
