# @Time : 2021/1/28 10:26
# @Author:曹晶晶
# 　＠File : 02.发送post请求.py
import requests

# 表单格式的数据：content-type：www-x-form-urlencoded ，使用data传参
#
# url = "http://jy001:8081/futureloan/mvc/api/member/login"
# cs = {
#     "mobilephone": "13073514021", "pwd": "123",
# }
# r = requests.post(url, data=cs)
# print(r.text)
# rjson = r.json()
# assert rjson["status"] == 0
# print(rjson["msg"])
#
# # jsoon格式的数据：content-type:application/json,使用json传参
# # 具体使用data还是json传参，要看接口怎么定义
# # httpbin.org 是一个测试网站，封装成json格式的返回
# url = "http://www.httpbin.org/post"
# cs = { "mobilephone": "13073514021", "pwd": "123" }
# r = requests.post(url,data=cs)
# print("data传参====",r.text)
# r = requests.post(url,json=cs)
# print("json传参===",r.text)

# 租车系统，通过接口添加车
url = "http://localhost:8080/carRental/car/addCar.action"
# 请求头
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
cs = {
    "carnumber": "晋A6655",
    "cartype": "小轿车",
    "color": "黑色",
    "carimg": r"D:\ApiAutoTest\day01\1.png",
    "description": "外观漂亮",
    "price": "450000",
    "rentprice": "4000",
    "deposit": "1000",
    "isrenting": "0",
}
# Fidder 抓脚本，设置代理
proxy = {
    "http": "http://127.0.0.1:8888", #http协议，使用这个代理
    "https": "http://127.0.0.1:8888" #https协议，使用这个代理
}
r = requests.post(url, data=cs, headers=headers,proxies=proxy)
print(r.text)
rjson = r.json()
assert rjson["code"] == 0
