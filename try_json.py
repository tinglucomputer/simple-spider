# coding-utf8
# 百度翻译 在手机版形式下 刷新一下就变过来了
# 一般手机版形式下会返回json串  现在网站都设置了反爬虫机制 不能随随便便的对一个请求响应
import requests
import json

url = "https://fanyi.baidu.com/basetrans"

translate_str = input("请输入要翻译的中文字符串：")

query_string = {"query": translate_str,
                "from": "zh",
                "to": "en",
                }

cookies_str = "BIDUPSID=4C4A853BD2957DCF81EEFA4238641E9C; " \
              "PSTM=1581233806; BAIDUID=4C4A853BD2957DCF1202F0810E445835; " \
              "FG=1; REALTIME_TRANS_SWITCH=1; " \
              "FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; " \
              "SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; " \
              "BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; " \
              "from_lang_often=%5B%7B%22value%22%3A%22slo%22%2C%22text%22%3A%22%u65AF%u6D1B%u6587%u5C3C%u4E9A%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; " \
              "H_WISE_SIDS=139561_127760_128698_141256_135847_141000_125125_141098_138904_141707_133995_138878_137979_141200_140173_131247_137745_138165_107314_138883_140260_141754_139050_140202_136863_138585_141651_138252_140114_131861_141743_140324_140578_133847_140793_140065_134046_131423_140368_140798_138661_136413_141104_110085_141942_127969_141110_140593_140865_139886_138425_139557_141190; " \
              "H_PS_PSSID=30745_1451_21080_30724; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; delPer=0; PSINO=2; yjsv5_shitong=1.0_7_413b2f4a80d0835c42d3f48b07f47be06454_300_1581467524697_27.207.59.82_140695a9; yjs_js_security_passport=54a02536b29a271a20d3421acaac8706a678c3b6_1581467525_js; " \
              "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1581467333,1581467394,1581467527,1581467588; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1581467588; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1581467588; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1581467588"

cookies_dict = {i.split("=")[0]: i.split("=")[1] for i in cookies_str.split("; ")}

print(cookies_dict)

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                         "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 "
                         "Mobile/15A372 Safari/604.1"}

response = requests.post(url, data=query_string, headers=headers, cookies=cookies_dict)    # post请求

print(response)

html_str = response.content.decode()

dict_ret = json.loads(html_str)     # html_str一定是json类型的字符串,如果是xml格式的不能解析,解析的结果是字典

json_str1 = json.dumps({"a": "a", "b": 2})  # 把python字典转化为json字符串,以便写入到本地展示

print(json_str1)
print(dict_ret)

