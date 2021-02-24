# @Time : 2021/1/28 9:39
# @Author:曹晶晶
# 　＠File : 01.发送get请求.py
"""接口测试：
    使用request中的个头、post方法调用接口，检查返回值是否正确
"""
import requests

###################################get请求，不带参数###########################################
# 获取用户列表
url = "http://jy001:8081/futureloan/mvc/api/member/list"
r = requests.get(url)
# 打印响应
print(r.text)
# 断言
assert r.status_code == 200, "断言失败"
assert r.reason == "OK"
rjson = r.json()  # 转化为json格式，响应体
assert rjson["status"] == 1
assert rjson["code"] == "10001"

# 响应头
print(r.headers)

'''注册接口'''

###################################get请求，带参数###########################################
# get请求，带参数 ，参数拼接到URL后面？后面是参数，多个参数用&连接
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=12345678909&pwd=123"
r = requests.get(url)
print(r.text)
rjson = r.json()
assert rjson["status"] == 0

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13073514021", "pwd": "123456",
      "regname": "request_name"
      }
re = requests.get(url, params=cs)  # 传入参数
print(re.text)
rjson = re.json()
assert rjson["status"] == 0
assert rjson["code"] == "20110"
assert rjson["msg"] == "手机号码已被注册"
# post
re = requests.post(url, data=cs)
print(re.text)

#
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
phone = {
    "tel": "18435336869"
}
r = requests.get(url, params=phone)
print(r.text)
assert "山西移动" in r.text
