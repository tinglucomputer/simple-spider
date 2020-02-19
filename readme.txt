本工程主要实现一个简单的爬虫程序
爬虫就是模拟浏览器（客户端）来发送访问请求,获取响应,按照规则提取数据的程序
最终爬的数据可以直接呈现给用户,也可以把数据用于分析等
1.浏览器请求
    url中包含了协议HTTP/HTTPS+网站的域名+资源的路径+参数
    浏览器请求url地址
        会得到当前url地址的响应+CSS渲染+JS渲染 = Element中的内容
    爬虫请求URL地址
        只会得到当前url地址的响应 = Response中的内容
        并不会把CSS和JS渲染过来
    因此,在实际开发过程中需要对element和response中内容加以区分
    如何找到当前网页url地址及其协议参数
        chrome浏览器->检查->network->里面有很多的响应,在response或者preview中查找有关返回的内容,有正确响应结果的是所寻找的
        ->header内有请求和响应的相关参数
2.认识HTTP和HTTPS协议
    HTTP以明文的形式传输,效率更高,但是并不安全
    HTTPS = HTTP + SSL(安全套接字层)需要对明文进行加减密
    get和post请求的区别:
        1.get请求没有请求体,post有,get请求把参数放在url地址中
        2.post请求常用于登录注册,post请求携带的数据量一般会比较大,比如翻译,
    HTTP协议之请求:
        1.请求行   请求的方法GET/POST+部分URL+协议
        2.请求头
            host:与请求行中的部分URL合并在一起共同组成一个完整的URL,host更多的表示一个服务器或者目的端的地址,
                请求行中更多的想表示页面在服务器端的地址和请求参数
            user-agent:指明请求的客户端类型,是哪一种浏览器,是网页端还是手机端,
            cookie:存储在本地，记录了第一次访问时状态,一般都是用在登录上,服务器端还能据此知道请求是否是一个爬虫
            referer
         3.请求体
    HTTP协议之响应:
        1.响应行   协议+状态码
        2.响应头   set-cookie:设置在本地的cookie字段
        3.响应体
3.主要用到的模块和函数
4.数据的提取方式:json和xpath
    1.json:看起来像Python类型(列表和字典)的字符串,不过user-agent是手机端
    requests.get()/post().content.decode()返回的形式是json字符串,在形式上是Key-Value,却不是一个字典
        常用的方法是:
        json.loads():把json字符串转化为python字符串
        json.dumps():把python列表转化为json字符串
            常用的额外参数有
                ensure_ascii:显示中文
                indent:可以在显示时缩进
    2.xpath:一种从html标签中提取数据的高级语言
        语法:使用XPath helper插件,帮助我们在element中选中数据
        /:表示的下一级标签
        //:表示任意的下级标签
        ./:表示当前标签结点的下一级标签,一般都会在之前的语句中使用过xpath()函数
        @:可以和[]一起使用选择特定的标签,也可以单独使用提取标签内的属性值
            //div[@class='a']:表示只选择class=a的div标签,其他的div标签不予选中
                可以使用class,如果想获取唯一的标签使用id属性
            //div/a/@href:表示提取a标签的href属性值
        获取文本
            //a/text():表示获取a标签的文本
            //a//text():表示获取a标签全部的文本,往往a标签下有span标签
            [注]span标签一般用于修饰行内文字
总结:
1.url
    知道url地址的规律和总的页数:构造url_list
    如果不知道,就需要在程序中动态的构造url
2.发送请求,获取响应
    就是requests模块干的事
3.提取数据
    返回的是json字符串,就使用json模块
    返回的是html字符串,就使用lxml模块+xpath语法
4.保存数据


