# @Time : 2021/1/28 16:29
# @Author:曹晶晶
# 　＠File : 06.timeout.py
'''
1.上传文件接口，上传1M的文件和上传2G的文件，耗时不一样，默认的超时时间不够用时，可以设置接口超时
2.接口性能测试，看接口是否在某个时间内返回
'''
import requests
for i in range(10):
    try:
        r = requests.get("http://jy001:8081/futureloan/mvc/api/member/list",timeout=0.1) # 0.1 = 10ms
        print(r.text)
    except Exception as e:
        print(e)

# 租车系统上传