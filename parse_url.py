# 本程序体验超时参数的使用
from retrying import retry
import requests

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                         "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 "
                         "Mobile/15A372 Safari/604.1",
           "Referer": "https://m.douban.com/movie/"}

time = 1
@retry(stop_max_attempt_number=3)     # 被装饰的函数可以执行3次,中间有一次执行成功,程序可以继续往下执行,对错误的处理可以在函数内也可在函数外
def _parse_url(url):
    print("$"*5)
    response = requests.get(url, headers=headers, timeout=time)    # 如果经过一段时间后不能返回数据则请求失败
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "http://www.baidu.com"

    print(parse_url(url))