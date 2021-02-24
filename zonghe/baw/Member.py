# @Time : 2021/2/23 14:05
# @Author:曹晶晶
# 　＠File : Member.py

'''金融项目用户管理模块的接口
member 是模块名
list 是接口名
http://192.168.1.64:8089/futureloan/mvc/api/member/list
'''


# 业务层
def register(baserequest, url, data):
    url = url + "futureloan/mvc/api/member/register"
    r = baserequest.post(url, data=data)
    return r


def list(baserequest, url):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequest.post(url)
    return r


def login(baserequest, url, data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequest.post(url, data=data)
    return r


def delete(baserequest, url, data):
    url = url + "futureloan/mvc/api/member/delete"
    r = baserequest.post(url, data=data)
    return r


def recharge(baserequest, url, data):
    url = url + "futureloan/mvc/api/member/recharge"
    r = baserequest.post(url, data=data)
    return r
