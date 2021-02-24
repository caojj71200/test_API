# @Time : 2021/1/28 15:17
# @Author:曹晶晶
# 　＠File : 04.手动添加Cookie.py

'''Cookie 用来识别用户'''
import requests

# 没有登录时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r)
# 登录时返回cookie信息，带上cookie信息
headers = {
    "Cookie": '_ga=GA1.2.1148882396.1611729674; _gid=GA1.2.838047120.1611729674; __auc=0b57b989177429321f81826e4d0; MEIQIA_TRACK_ID=1ndpdUOxOWW8Loh7Bd5AD831G2y; MEIQIA_VISIT_ID=1ndpdSzbM8qvDyBIYUal03t0eSB; __asc=f9cd997217747de3863546287b1; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611729674,1611729905,1611730449,1611818482; BAGSESSIONID=2be6272c-c56d-4767-8af8-490a3f08b278; JSESSIONID=599542F413AFA2E0FD2F04E31374B0A2; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611818511',
}
re = requests.get(url, headers=headers)
print(re.text)
assert "<title>百格活动 - 账户总览</title>" in re.text
'''
缺点：
1.cookie会失败，失效后需要重新获取
2.登录后的每个接口，需要带着cookie
'''
