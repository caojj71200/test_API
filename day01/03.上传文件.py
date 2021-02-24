# @Time : 2021/1/28 14:02
# @Author:曹晶晶
# 　＠File : 03.上传文件.py

import requests

# 添加图片
# url = "http://www.httpbin.org/post"
url = "http://localhost:8080/carRental/file/uploadFile.action"
# 本地存放的文件
file = r"D:\ApiAutoTest\day01\img\b1.png"
# rb 二进制只读的方式打开
with open(file, mode='rb') as f:
    # {'name':file -tuple}
    # file-tuple：{filename,fileobj,content_type}
    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)
    uploadPath = r.json()["data"]["src"]

# 添加车

url = "http://localhost:8080/carRental/car/addCar.action"
# 请求头
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
cs = {
    "carnumber": "晋A8822",
    "cartype": "小轿车",
    "color": "黑色",
    "carimg": uploadPath,
    "description": "外观漂亮",
    "price": "450000",
    "rentprice": "4000",
    "deposit": "1000",
    "isrenting": "0",
}
# Fidder 抓脚本，设置代理
proxy = {
    "http": "http://127.0.0.1:8888",  # http协议，使用这个代理
    "https": "http://127.0.0.1:8888"  # https协议，使用这个代理
}
r = requests.post(url, data=cs, headers=headers, proxies=proxy)
print(r.text)
rjson = r.json()
assert rjson["code"] == 0
