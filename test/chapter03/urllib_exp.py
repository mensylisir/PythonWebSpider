from urllib.request import quote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
# from urllib.request import urlunparse
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'id=6', 'comment']
# print(urlunparse(data))
# from urllib import request, error
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.html')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)
# import http.cookiejar
# import urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')

# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
#
# proxy_handler = ProxyHandler({
#     'http':'http://127.0.0.1:9999',
#     'https':'https://127.0.0.1:9999'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e)



# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from  urllib.error import URLError
#
# url = "http://localhost:8080"
# username = 'user'
# password = 'passwd'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
# try:
#     result = opener.open(url)
#     response = result.read(.decode('utf8'))
#     print(response)
# except URLError as e:
#     print(e)



# url = 'http://httpbin.org/post'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
#     'Host': 'httpbin.org'
# }
#
# param = {
#     "name": 'Germey'
# }
#
# data = bytes(urllib.parse.urlencode(param), encoding='utf8')
# req = urllib.request.Request(url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# try:
#     response = urllib.request.urlopen('http://httpbin.org/post', timeout=0.1)
#     print(response.read())
# except urllib.error.HTTPError as e:
#     print(e)


# param = {'world': 'hello'}
# data = bytes(urllib.parse.urlencode(param), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# response = urllib.request.urlopen("https://www.python.org")
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))
