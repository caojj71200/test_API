# @Time : 2021/1/28 15:37
# @Author:曹晶晶
# 　＠File : 05.自动管理Cookie.py
# '''
# requests.session 来保持状态，自动管理过程中产生的cookie
# 下一次请求时自动带上上一次的cookie
# '''
import requests
import requests.utils
s = requests.session()
print(s.cookies)
print("登录前的cookie", requests.utils.dict_from_cookiejar(s.cookies))
url = "https://www.bagevent.com/user/login"
cs = {
    "account": "2780487875@qq.com",
    "password": "qq2780487875"
}
# 登录接口
r = s.post(url, data=cs)
# print(r.text)

# bashboard
r = s.get("https://www.bagevent.com/account/dashboard")
print(r.text)

# 退出接口
url = "https://www.bagevent.com/user/login_out"
s.get(url)
print(s.cookies)
print("登录后的cookie", requests.utils.dict_from_cookiejar(s.cookies))
