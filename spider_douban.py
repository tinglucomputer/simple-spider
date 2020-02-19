import json
import requests

url = "https://m.douban.com/rexxar/api/v2/movie/suggestion?start=0&count=10&new_struct=1&with_review=1&for_mobile=1"

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                         "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 "
                         "Mobile/15A372 Safari/604.1",
           "Referer": "https://m.douban.com/movie/"}    # Referer字段用于浏览器向服务器发送请求时指出的请求地址

response = requests.get(url, headers=headers, )     # 在headers中不加Referer字段直接请求会报错

json_str = response.content.decode()    # 中文显示不出来

# print(json_str)

json_dict = json.loads(json_str)    # 字典形式,能显示中文

with open("douban.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(json_dict, ensure_ascii=False, indent=2))

# print(json_dict)
