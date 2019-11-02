from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = 'mensyli4:Xy1234!@#@127.0.0.0:7453'
proxy_handler = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e)
