# 本程序主要是体验一下使用cookie用于登录
# 人人网 登录账号 15865938701 密码 dongtinglu1996
# 也可借助session来完成

import requests

url = "http://www.renren.com/PLogin.do"

data = {"email": "15865938701",
        "password": "dongtinglu1996"}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

response = requests.post(url, data=data, headers=headers)

for i in response.request.headers.items():
    if i[0] in "Cookie":
        print(i)
        break

cookis_dict = {i.split("=")[0]: i.split("=")[1] for i in i[1].split("; ")}  # 使用的是字典推导式

response = requests.get(url, headers=headers, cookies=cookis_dict)

with open("renren1.html", "w", encoding="utf-8") as f:

    f.write(response.content.decode())


