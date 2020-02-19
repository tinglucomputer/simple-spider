from lxml import etree
import requests

url = "https://movie.douban.com/chart"

# 电脑版
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

reponse = requests.get(url, headers=headers, )

html_str = reponse.content.decode()

# 使用etree处理数据
html = etree.HTML(html_str)

# print(html)  # Element

# 返回的结果是Response,我们在网页上比对的是Elements,因此在写xpath语法时要小心
url_list = html.xpath("//div[@class='indent']//table//a[@class='nbg']/@href")


# 把每一部电影的属性都提取出来形成一个字典的形式
# 思路:1.找到这些记录的最低公共祖先标签  2.分组提取所想获得的字段
table_list = html.xpath("//div[@class='indent']//table")

# print(table_list)   # Element list

for i in table_list:
    item = {}
    item["title"] = i.xpath(".//div[@class='pl2']/a/text()")[0].replace("/", "").strip()
    item["href"] = i.xpath(".//div[@class='pl2']/a/@href")
    item["img"] = i.xpath(".//a[@class='nbg']/img/@src")
    item["comment_score"] = i.xpath(".//span[@class='pl']/text()")
    item["rating_score"] = i.xpath(".//span[@class='rating_nums']/text()")
    print(item)


