import requests
from lxml import etree  #pip install lxml xpath

login_page_url = "https://passport.5i5j.com/passport/login?service=https%3A%2F%2Fbj.5i5j.com%2Freglogin%2Findex%3FpreUrl%3Dhttps%253A%252F%252Fbj.5i5j.com%252F%253Fpmf_group%253Dbaidu%2526pmf_medium%253Dppzq%2526pmf_plan%253D%2525E5%2525B7%2525A6%2525E4%2525BE%2525A7%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_unit%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_keyword%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_account%253D160&status=1&city=bj"

login_page_headers = {
     "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
}
# 获取cookie
#requts 模es块可以用来写爬虫，但是request模块请求服务器默认不保存cookie

request = requests.session()#这个方法开启一个保存cookie的请求器
response = request.get(url=login_page_url, headers = login_page_headers)
content = response.content.decode()

# 获取处理用户名和密码之外的三项提交的值
html = etree.HTML(content)

aim = html.xpath('//input[@id="aim1"]')[0].attrib["value"]
service  = html.xpath('//input[@id="service"]')[0].attrib["value"]
status = html.xpath('//input[@id="status1"]')[0].attrib["value"]


#2、对获取的数据进行总结，携带完整请求数据和cookie请求登录接口，完成模拟登录
#对获取的数据进行总结，携带完整请求数据和cookie请求登录接口，完成模拟登录

login_data = {
    "aim":aim,
    "service":service,
    "status":status,
    "username":"13191878042",
    "password":"django2018"
}

login_url = "https://passport.5i5j.com/passport/sigin?city=bj"
login_headers = {
    "Referer": login_page_url,
    "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
}
login__response = request.post(url=login_url, headers = login_headers, data=login_data)

login_result = login__response.content.decode()

print(login_result)










