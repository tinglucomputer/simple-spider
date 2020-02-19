# 本程序是一个实例,爬取豆瓣上的电影内容
import json
from parse_url import parse_url


class DoubanSpider:

    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/movie/suggestion?start={}&count=10&new_struct=1&with_review=1&for_mobile=1"

    def get_content_list(self, html_str):
        dict_data = json.loads((html_str))
        content_list = dict_data["items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
        with open("douban.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def run(self):
        num = 0
        total = 100
        while num < total + 10:  # 这个循环条件是非常需要注意的
            # 1.设置请求的URL地址
            url = self.temp_url.format(num)
            # 2.解析地址,返回网页源码形式的json字符串
            html_str = parse_url(url)
            print(url)
            # 3.json字符串转化为字典,提取有用的内容
            content_list, total = self.get_content_list(html_str)
            # 4.把想要的内容再转化为json串,记录到本地或者回写到浏览器
            self.save_content_list(content_list)
            # 5.构造新的URL地址,提取下一单元记录
            num += 10

if __name__ == '__main__':
    douban = DoubanSpider()     # 实例化一个对象

    douban.run()

